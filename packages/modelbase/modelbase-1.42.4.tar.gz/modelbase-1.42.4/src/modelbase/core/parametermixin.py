from __future__ import annotations

__all__ = [
    "Parameter",
    "ParameterMixin",
]

import json
import pickle
import warnings
from dataclasses import dataclass, field
from queue import Empty, SimpleQueue
from typing import Any, Callable, Dict, Iterable, List, Optional

import libsbml
from typing_extensions import Literal  # 3.7 compatability

from .basemodel import BaseModel
from .utils import (
    convert_id_to_sbml,
    get_formatted_function_source_code,
    warning_on_one_line,
)

warnings.formatwarning = warning_on_one_line  # type: ignore


@dataclass
class Parameter:
    """Meta-info container for parameters."""

    unit: Optional[str] = None
    annotation: Optional[str] = None
    database_links: dict = field(default_factory=dict)
    notes: dict = field(default_factory=dict)


@dataclass
class DerivedParameter:
    function: Callable
    parameters: list[str]

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]


class ParameterMixin(BaseModel):
    """Adding parameter functions."""

    def __init__(self, parameters: dict[str, float] | None = None) -> None:
        self.derived_parameters: dict[str, DerivedParameter] = {}
        self._parameters: dict[str, float] = {}
        self._derived_parameter_order: list[str] = []

        # Bookkeeping
        self._derived_from_parameters: set[str] = set()

        if parameters is not None:
            self.add_parameters(parameters=parameters)
        self.initialization_parameters = self._parameters.copy()

    @property
    def parameters(self) -> dict[str, float]:
        return self.get_all_parameters()

    ##########################################################################
    # Meta info
    ##########################################################################

    def _add_parameter_meta_info(self, parameter: str, meta_info: dict) -> None:
        self.meta_info.setdefault("parameters", {}).setdefault(
            parameter,
            Parameter(**meta_info),  # type: ignore
        )

    def update_parameter_meta_info(self, parameter: str, meta_info: dict) -> None:
        """Update meta info of a parameter.

        Parameters
        ----------
        meta_info
            Meta info of the parameter. Allowed keys are
            {unit, database_links, notes}
        """
        self.update_meta_info(component="parameters", meta_info={parameter: meta_info})

    ##########################################################################
    # Parameter functions
    ##########################################################################

    def add_parameter(
        self,
        parameter_name: str,
        parameter_value: float,
        update_derived: bool = True,
        **meta_info: Dict[str, Any],
    ) -> None:
        """Add a new parameter to the model.

        Parameters
        ----------
        meta_info
            Meta info of the parameter. Allowed keys are
            {unit, database_links, notes}
        """
        self._check_and_insert_ids([parameter_name], context="add_parameter")
        self._add_parameter_meta_info(parameter_name, meta_info)

        self._parameters[parameter_name] = parameter_value

    def add_parameters(
        self,
        parameters: Dict[str, float],
        meta_info: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Add multiple parameters to the model"""
        meta_info = {} if meta_info is None else meta_info
        for parameter_name, parameter_value in parameters.items():
            info = meta_info.get(parameter_name, {})
            self.add_parameter(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
                **info,
            )

    def update_parameter(
        self,
        parameter_name: str,
        parameter_value: float,
        update_derived: bool = True,
        **meta_info: Dict[str, Any],
    ) -> None:
        """Update an existing model parameter.

        Warns
        -----
        UserWarning
            If parameter is not in the model
        """
        if parameter_name not in self._parameters:
            if parameter_name in self._derived_from_parameters:
                raise ValueError(f"{parameter_name} is a derived parameter")
            warnings.warn(f"Key {parameter_name} is not in the model. Adding.")
        self.update_parameter_meta_info(parameter_name, meta_info)
        self._parameters[parameter_name] = parameter_value

    def scale_parameter(self, parameter_name: str, factor: float) -> None:
        self.update_parameter(parameter_name, self._parameters[parameter_name] * factor)

    def update_parameters(
        self,
        parameters: Dict[str, float],
        meta_info: Dict[str, Dict[str, Any]] | None = None,
    ) -> None:
        """Update multiple existing model parameters.

        See Also
        --------
        update_parameter
        """
        meta_info = {} if meta_info is None else meta_info
        for parameter_name, parameter_value in parameters.items():
            info = meta_info.get(parameter_name, {})
            self.update_parameter(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
                **info,
            )

    def add_and_update_parameter(
        self,
        parameter_name: str,
        parameter_value: float,
        update_derived: bool = True,
        **meta_info: Dict[str, Any],
    ) -> None:
        """Add a new or update an existing parameter."""
        if parameter_name not in self._ids:
            self.add_parameter(
                parameter_name, parameter_value, update_derived, **meta_info
            )
        else:
            self.update_parameter(
                parameter_name, parameter_value, update_derived, **meta_info
            )

    def add_and_update_parameters(
        self,
        parameters: Dict[str, float],
        meta_info: Dict[str, Dict[str, Any]] | None = None,
    ) -> None:
        """Add new and update existing model parameters.

        See Also
        --------
        add_and_update_parameter
        """
        meta_info = {} if meta_info is None else meta_info
        for parameter_name, parameter_value in parameters.items():
            info = meta_info.get(parameter_name, {})
            self.add_and_update_parameter(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
                **info,
            )

    def remove_parameter(self, parameter_name: str) -> None:
        """Remove a parameter from the model."""
        del self._parameters[parameter_name]
        if parameter_name in self.meta_info:
            del self.meta_info["parameters"][parameter_name]
        self._remove_ids([parameter_name])

    def remove_parameters(self, parameter_names: Iterable[str]) -> None:
        """Remove multiple parameters from the model.

        See Also
        --------
        remove_parameter
        """
        for parameter_name in parameter_names:
            self.remove_parameter(parameter_name=parameter_name)

    ##########################################################################
    # Derived parameter functions
    ##########################################################################

    def _sort_derived_parameters(self, max_iterations: int = 10_000) -> None:
        available = set(self.get_parameter_names())
        par_order = []
        pars_to_sort: SimpleQueue = SimpleQueue()
        for k, v in self.derived_parameters.items():
            pars_to_sort.put((k, v.parameters))

        last_name = None
        i = 0
        while True:
            try:
                name, args = pars_to_sort.get_nowait()
            except Empty:
                break
            if name in available:
                available.update(args)
                par_order.append(name)
            else:
                if last_name == name:
                    par_order.append(name)
                    break
                pars_to_sort.put((name, args))
                last_name = name
            i += 1
            if i > max_iterations:
                to_sort = []
                while True:
                    try:
                        to_sort.append(pars_to_sort.get_nowait()[0])
                    except Empty:
                        break

                raise ValueError(
                    "Exceeded max iterations on derived parameter module sorting. "
                    "Check if there are circular references.\n"
                    f"Available: {to_sort}\n"
                    f"Order: {par_order}"
                )
        self._derived_parameter_order = par_order

    def add_derived_parameter(
        self,
        parameter_name: str,
        function: Callable,
        parameters: List[str],
        **meta_info: Dict[str, Any],
    ) -> None:
        """Add a derived parameter.

        Derived parameters are calculated from other model parameters and dynamically updated
        on any changes.
        """
        # Do this first to check if all parameters are actually in the model
        # Since we also need the values to compute anything, don't use _check_for_existence here
        # that would be an unnecessary duplicate effort
        parameter_values = [self._parameters[i] for i in parameters]

        self.derived_parameters[parameter_name] = DerivedParameter(
            function=function,
            parameters=parameters,
        )
        for parameter in parameters:
            self._derived_from_parameters.add(parameter)

        # Initial calculation
        self.add_parameter(
            parameter_name=parameter_name,
            parameter_value=function(*parameter_values),
            update_derived=True,
            **meta_info,
        )

        self._sort_derived_parameters()

    def update_derived_parameter(
        self,
        parameter_name: str,
        function: Callable | None,
        parameters: List[str] | None,
        **meta_info: Dict[str, Any],
    ) -> None:
        old = self.derived_parameters[parameter_name]
        if function is None:
            function = old.function
        if parameters is None:
            parameters = old.parameters

        self.derived_parameters[parameter_name].function = function
        self.derived_parameters[parameter_name].parameters = parameters
        self.update_parameter_meta_info(parameter_name, meta_info)
        self._sort_derived_parameters()

    def remove_derived_parameter(self, parameter_name: str) -> None:
        """Remove a derived parameter from the model."""
        old_parameter = self.derived_parameters.pop(parameter_name)
        derived_from = old_parameter["parameters"]
        for i in derived_from:
            if all(i not in j["parameters"] for j in self.derived_parameters.values()):
                self._derived_from_parameters.remove(i)
        self.remove_parameter(parameter_name=parameter_name)
        self._sort_derived_parameters()

    def store_parameters_to_file(
        self,
        filename: str,
        filetype: Literal["json", "pickle"] = "json",
    ) -> None:
        """Store the parameters into a json or pickle file."""
        if filetype == "json":
            if not filename.endswith(".json"):
                filename += ".json"
            with open(filename, "w") as f:
                json.dump(self._parameters, f)
        elif filetype == "pickle":
            if not filename.endswith(".p"):
                filename += ".p"
            with open(filename, "wb") as f:  # type: ignore
                pickle.dump(self._parameters, f)  # type: ignore
        else:
            raise ValueError("Can only save to json or pickle")

    def load_parameters_from_file(
        self,
        filename: str,
        filetype: Literal["json", "pickle"] = "json",
    ) -> None:
        """Load parameters from a json or pickle file."""
        if filetype == "json":
            with open(filename, "r") as f:
                self.add_and_update_parameters(parameters=json.load(f))
        elif filetype == "pickle":
            with open(filename, "rb") as f:  # type: ignore
                self.add_and_update_parameters(parameters=pickle.load(f))  # type: ignore
        else:
            raise ValueError("Can only load from json or pickle")

    def restore_initialization_parameters(self) -> None:
        """Restore parameters to initialization parameters."""
        self._parameters = self.initialization_parameters.copy()

    def get_parameter(self, parameter_name: str) -> float:
        """Return the value of a single parameter."""
        return float(self._parameters[parameter_name])

    def get_parameters(self) -> Dict[str, float]:
        """Return all parameters."""
        return dict(self._parameters)

    def get_all_parameters(self) -> dict[str, float]:
        all_params = self._parameters.copy()

        for parameter_name in self._derived_parameter_order:
            derived_parameter = self.derived_parameters[parameter_name]
            all_params[parameter_name] = derived_parameter.function(
                *(all_params[i] for i in derived_parameter.parameters)
            )

        return all_params

    def get_parameter_names(self) -> List[str]:
        """Return names of all parameters"""
        return list(self._parameters)

    def get_all_parameter_names(self) -> set[str]:
        """Return names of all parameters"""
        return set(self._parameters) | set(self.derived_parameters)

    ##########################################################################
    # Source code functions
    ##########################################################################
    def _generate_constant_parameters_source_code(
        self, *, include_meta_info: bool = True
    ) -> str:
        """Generate modelbase source code for parameters.

        This is mainly used for the generate_model_source_code function.

        Parameters
        ----------
        include_meta_info : bool
            Whether to include the parameter meta info

        Returns
        -------
        parameter_modelbase_code : str
            Source code generating the modelbase parameters
        """
        parameters = repr({k: v for k, v in self._parameters.items()})
        # derived_pars =
        if include_meta_info:
            meta_info = self._get_nonzero_meta_info(component="parameters")
            if bool(meta_info):
                return f"m.add_parameters(parameters={parameters}, meta_info={meta_info})"
        return f"m.add_parameters(parameters={parameters})"

    def _generate_derived_parameters_source_code(self) -> tuple[str, str]:
        """Generate modelbase source code for parameters.

        This is mainly used for the generate_model_source_code function.

        Parameters
        ----------
        include_meta_info : bool
            Whether to include the parameter meta info

        Returns
        -------
        parameter_modelbase_code : str
            Source code generating the modelbase parameters
        """
        fns: set[str] = set()
        pars: list[str] = []
        for name, module in self.derived_parameters.items():
            function = module["function"]
            parameters = module["parameters"]

            function_code = get_formatted_function_source_code(
                function_name=name, function=function, function_type="module"
            )
            fns.add(function_code)
            pars.append(
                (
                    "m.add_derived_parameter(\n"
                    f"    parameter_name={repr(name)},\n"
                    f"    function={function.__name__},\n"
                    f"    parameters={parameters},\n"
                    ")"
                )
            )
        return "\n".join(sorted(fns)), "\n".join(pars)

    def _generate_parameters_source_code(
        self, *, include_meta_info: bool = True
    ) -> tuple[str, str, str]:
        return (
            self._generate_constant_parameters_source_code(
                include_meta_info=include_meta_info
            ),
            *self._generate_derived_parameters_source_code(),
        )

    ##########################################################################
    # SBML functions
    ##########################################################################

    def _create_sbml_parameters(self, *, sbml_model: libsbml.Model) -> None:
        """Create the parameters for the sbml model.

        Parameters
        ----------
        sbml_model : libsbml.Model
        """
        for parameter_id, value in self._parameters.items():
            parameter = self.meta_info["parameters"][parameter_id]
            k = sbml_model.createParameter()
            k.setId(convert_id_to_sbml(id_=parameter_id, prefix="PAR"))
            k.setConstant(True)
            k.setValue(float(value))
            unit = parameter.unit
            if unit is not None:
                k.setUnits(unit)
