from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.field_definitions_link import FieldDefinitionsLink
from ..models.workflow_task_schema_dependency_link_output import WorkflowTaskSchemaDependencyLinkOutput
from ..models.workflow_task_schema_dependency_link_type import WorkflowTaskSchemaDependencyLinkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowTaskSchemaDependencyLink")


@attr.s(auto_attribs=True, repr=False)
class WorkflowTaskSchemaDependencyLink:
    """  """

    _type: WorkflowTaskSchemaDependencyLinkType
    _name: str
    _resource_id: Optional[str]
    _output: Union[Unset, WorkflowTaskSchemaDependencyLinkOutput] = UNSET
    _field_definitions: Union[Unset, List[FieldDefinitionsLink]] = UNSET
    _description: Union[Unset, None, str] = UNSET
    _required_config: Union[Unset, bool] = False
    _resource_name: Union[Unset, None, str] = UNSET

    def __repr__(self):
        fields = []
        fields.append("type={}".format(repr(self._type)))
        fields.append("name={}".format(repr(self._name)))
        fields.append("resource_id={}".format(repr(self._resource_id)))
        fields.append("output={}".format(repr(self._output)))
        fields.append("field_definitions={}".format(repr(self._field_definitions)))
        fields.append("description={}".format(repr(self._description)))
        fields.append("required_config={}".format(repr(self._required_config)))
        fields.append("resource_name={}".format(repr(self._resource_name)))
        return "WorkflowTaskSchemaDependencyLink({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        type = self._type.value

        name = self._name
        resource_id = self._resource_id
        output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self._output, Unset):
            output = self._output.to_dict()

        field_definitions: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._field_definitions, Unset):
            field_definitions = []
            for field_definitions_item_data in self._field_definitions:
                field_definitions_item = field_definitions_item_data.to_dict()

                field_definitions.append(field_definitions_item)

        description = self._description
        required_config = self._required_config
        resource_name = self._resource_name

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if output is not UNSET:
            field_dict["output"] = output
        if field_definitions is not UNSET:
            field_dict["fieldDefinitions"] = field_definitions
        if description is not UNSET:
            field_dict["description"] = description
        if required_config is not UNSET:
            field_dict["requiredConfig"] = required_config
        if resource_name is not UNSET:
            field_dict["resourceName"] = resource_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_type() -> WorkflowTaskSchemaDependencyLinkType:
            _type = d.pop("type")
            try:
                type = WorkflowTaskSchemaDependencyLinkType(_type)
            except ValueError:
                type = WorkflowTaskSchemaDependencyLinkType.of_unknown(_type)

            return type

        try:
            type = get_type()
        except KeyError:
            if strict:
                raise
            type = cast(WorkflowTaskSchemaDependencyLinkType, UNSET)

        def get_name() -> str:
            name = d.pop("name")
            return name

        try:
            name = get_name()
        except KeyError:
            if strict:
                raise
            name = cast(str, UNSET)

        def get_resource_id() -> Optional[str]:
            resource_id = d.pop("resourceId")
            return resource_id

        try:
            resource_id = get_resource_id()
        except KeyError:
            if strict:
                raise
            resource_id = cast(Optional[str], UNSET)

        def get_output() -> Union[Unset, WorkflowTaskSchemaDependencyLinkOutput]:
            output: Union[Unset, Union[Unset, WorkflowTaskSchemaDependencyLinkOutput]] = UNSET
            _output = d.pop("output")

            if not isinstance(_output, Unset):
                output = WorkflowTaskSchemaDependencyLinkOutput.from_dict(_output)

            return output

        try:
            output = get_output()
        except KeyError:
            if strict:
                raise
            output = cast(Union[Unset, WorkflowTaskSchemaDependencyLinkOutput], UNSET)

        def get_field_definitions() -> Union[Unset, List[FieldDefinitionsLink]]:
            field_definitions = []
            _field_definitions = d.pop("fieldDefinitions")
            for field_definitions_item_data in _field_definitions or []:
                field_definitions_item = FieldDefinitionsLink.from_dict(
                    field_definitions_item_data, strict=False
                )

                field_definitions.append(field_definitions_item)

            return field_definitions

        try:
            field_definitions = get_field_definitions()
        except KeyError:
            if strict:
                raise
            field_definitions = cast(Union[Unset, List[FieldDefinitionsLink]], UNSET)

        def get_description() -> Union[Unset, None, str]:
            description = d.pop("description")
            return description

        try:
            description = get_description()
        except KeyError:
            if strict:
                raise
            description = cast(Union[Unset, None, str], UNSET)

        def get_required_config() -> Union[Unset, bool]:
            required_config = d.pop("requiredConfig")
            return required_config

        try:
            required_config = get_required_config()
        except KeyError:
            if strict:
                raise
            required_config = cast(Union[Unset, bool], UNSET)

        def get_resource_name() -> Union[Unset, None, str]:
            resource_name = d.pop("resourceName")
            return resource_name

        try:
            resource_name = get_resource_name()
        except KeyError:
            if strict:
                raise
            resource_name = cast(Union[Unset, None, str], UNSET)

        workflow_task_schema_dependency_link = cls(
            type=type,
            name=name,
            resource_id=resource_id,
            output=output,
            field_definitions=field_definitions,
            description=description,
            required_config=required_config,
            resource_name=resource_name,
        )

        return workflow_task_schema_dependency_link

    @property
    def type(self) -> WorkflowTaskSchemaDependencyLinkType:
        if isinstance(self._type, Unset):
            raise NotPresentError(self, "type")
        return self._type

    @type.setter
    def type(self, value: WorkflowTaskSchemaDependencyLinkType) -> None:
        self._type = value

    @property
    def name(self) -> str:
        if isinstance(self._name, Unset):
            raise NotPresentError(self, "name")
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def resource_id(self) -> Optional[str]:
        if isinstance(self._resource_id, Unset):
            raise NotPresentError(self, "resource_id")
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value: Optional[str]) -> None:
        self._resource_id = value

    @property
    def output(self) -> WorkflowTaskSchemaDependencyLinkOutput:
        if isinstance(self._output, Unset):
            raise NotPresentError(self, "output")
        return self._output

    @output.setter
    def output(self, value: WorkflowTaskSchemaDependencyLinkOutput) -> None:
        self._output = value

    @output.deleter
    def output(self) -> None:
        self._output = UNSET

    @property
    def field_definitions(self) -> List[FieldDefinitionsLink]:
        if isinstance(self._field_definitions, Unset):
            raise NotPresentError(self, "field_definitions")
        return self._field_definitions

    @field_definitions.setter
    def field_definitions(self, value: List[FieldDefinitionsLink]) -> None:
        self._field_definitions = value

    @field_definitions.deleter
    def field_definitions(self) -> None:
        self._field_definitions = UNSET

    @property
    def description(self) -> Optional[str]:
        if isinstance(self._description, Unset):
            raise NotPresentError(self, "description")
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        self._description = value

    @description.deleter
    def description(self) -> None:
        self._description = UNSET

    @property
    def required_config(self) -> bool:
        if isinstance(self._required_config, Unset):
            raise NotPresentError(self, "required_config")
        return self._required_config

    @required_config.setter
    def required_config(self, value: bool) -> None:
        self._required_config = value

    @required_config.deleter
    def required_config(self) -> None:
        self._required_config = UNSET

    @property
    def resource_name(self) -> Optional[str]:
        if isinstance(self._resource_name, Unset):
            raise NotPresentError(self, "resource_name")
        return self._resource_name

    @resource_name.setter
    def resource_name(self, value: Optional[str]) -> None:
        self._resource_name = value

    @resource_name.deleter
    def resource_name(self) -> None:
        self._resource_name = UNSET
