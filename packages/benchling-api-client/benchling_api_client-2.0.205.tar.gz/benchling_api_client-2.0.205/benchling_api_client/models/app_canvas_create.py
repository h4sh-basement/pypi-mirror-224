from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError, UnknownType
from ..models.button_ui_block import ButtonUiBlock
from ..models.chip_ui_block import ChipUiBlock
from ..models.dropdown_ui_block import DropdownUiBlock
from ..models.markdown_ui_block import MarkdownUiBlock
from ..models.search_input_ui_block import SearchInputUiBlock
from ..models.section_ui_block import SectionUiBlock
from ..models.selector_input_ui_block import SelectorInputUiBlock
from ..models.text_input_ui_block import TextInputUiBlock
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppCanvasCreate")


@attr.s(auto_attribs=True, repr=False)
class AppCanvasCreate:
    """  """

    _app_id: str
    _enabled: Union[Unset, bool] = UNSET
    _feature_id: Union[Unset, str] = UNSET
    _resource_id: Union[Unset, str] = UNSET
    _session_id: Union[Unset, None, str] = UNSET
    _blocks: Union[
        Unset,
        List[
            Union[
                ButtonUiBlock,
                ChipUiBlock,
                DropdownUiBlock,
                MarkdownUiBlock,
                SearchInputUiBlock,
                SectionUiBlock,
                SelectorInputUiBlock,
                TextInputUiBlock,
                UnknownType,
            ]
        ],
    ] = UNSET

    def __repr__(self):
        fields = []
        fields.append("app_id={}".format(repr(self._app_id)))
        fields.append("enabled={}".format(repr(self._enabled)))
        fields.append("feature_id={}".format(repr(self._feature_id)))
        fields.append("resource_id={}".format(repr(self._resource_id)))
        fields.append("session_id={}".format(repr(self._session_id)))
        fields.append("blocks={}".format(repr(self._blocks)))
        return "AppCanvasCreate({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        app_id = self._app_id
        enabled = self._enabled
        feature_id = self._feature_id
        resource_id = self._resource_id
        session_id = self._session_id
        blocks: Union[Unset, List[Any]] = UNSET
        if not isinstance(self._blocks, Unset):
            blocks = []
            for blocks_item_data in self._blocks:
                if isinstance(blocks_item_data, UnknownType):
                    blocks_item = blocks_item_data.value
                elif isinstance(blocks_item_data, ButtonUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                elif isinstance(blocks_item_data, ChipUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                elif isinstance(blocks_item_data, DropdownUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                elif isinstance(blocks_item_data, MarkdownUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                elif isinstance(blocks_item_data, SearchInputUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                elif isinstance(blocks_item_data, SectionUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                elif isinstance(blocks_item_data, SelectorInputUiBlock):
                    blocks_item = blocks_item_data.to_dict()

                else:
                    blocks_item = blocks_item_data.to_dict()

                blocks.append(blocks_item)

        field_dict: Dict[str, Any] = {}
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if blocks is not UNSET:
            field_dict["blocks"] = blocks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_app_id() -> str:
            app_id = d.pop("appId")
            return app_id

        try:
            app_id = get_app_id()
        except KeyError:
            if strict:
                raise
            app_id = cast(str, UNSET)

        def get_enabled() -> Union[Unset, bool]:
            enabled = d.pop("enabled")
            return enabled

        try:
            enabled = get_enabled()
        except KeyError:
            if strict:
                raise
            enabled = cast(Union[Unset, bool], UNSET)

        def get_feature_id() -> Union[Unset, str]:
            feature_id = d.pop("featureId")
            return feature_id

        try:
            feature_id = get_feature_id()
        except KeyError:
            if strict:
                raise
            feature_id = cast(Union[Unset, str], UNSET)

        def get_resource_id() -> Union[Unset, str]:
            resource_id = d.pop("resourceId")
            return resource_id

        try:
            resource_id = get_resource_id()
        except KeyError:
            if strict:
                raise
            resource_id = cast(Union[Unset, str], UNSET)

        def get_session_id() -> Union[Unset, None, str]:
            session_id = d.pop("sessionId")
            return session_id

        try:
            session_id = get_session_id()
        except KeyError:
            if strict:
                raise
            session_id = cast(Union[Unset, None, str], UNSET)

        def get_blocks() -> Union[
            Unset,
            List[
                Union[
                    ButtonUiBlock,
                    ChipUiBlock,
                    DropdownUiBlock,
                    MarkdownUiBlock,
                    SearchInputUiBlock,
                    SectionUiBlock,
                    SelectorInputUiBlock,
                    TextInputUiBlock,
                    UnknownType,
                ]
            ],
        ]:
            blocks = []
            _blocks = d.pop("blocks")
            for blocks_item_data in _blocks or []:

                def _parse_blocks_item(
                    data: Union[Dict[str, Any]]
                ) -> Union[
                    ButtonUiBlock,
                    ChipUiBlock,
                    DropdownUiBlock,
                    MarkdownUiBlock,
                    SearchInputUiBlock,
                    SectionUiBlock,
                    SelectorInputUiBlock,
                    TextInputUiBlock,
                    UnknownType,
                ]:
                    blocks_item: Union[
                        ButtonUiBlock,
                        ChipUiBlock,
                        DropdownUiBlock,
                        MarkdownUiBlock,
                        SearchInputUiBlock,
                        SectionUiBlock,
                        SelectorInputUiBlock,
                        TextInputUiBlock,
                        UnknownType,
                    ]
                    discriminator_value: str = cast(str, data.get("type"))
                    if discriminator_value is not None:
                        if discriminator_value == "BUTTON":
                            blocks_item = ButtonUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "CHIP":
                            blocks_item = ChipUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "DROPDOWN":
                            blocks_item = DropdownUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "MARKDOWN":
                            blocks_item = MarkdownUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "SEARCH_INPUT":
                            blocks_item = SearchInputUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "SECTION":
                            blocks_item = SectionUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "SELECTOR_INPUT":
                            blocks_item = SelectorInputUiBlock.from_dict(data, strict=False)

                            return blocks_item
                        if discriminator_value == "TEXT_INPUT":
                            blocks_item = TextInputUiBlock.from_dict(data, strict=False)

                            return blocks_item

                        return UnknownType(value=data)
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = ButtonUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = ChipUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = DropdownUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = MarkdownUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = SearchInputUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = SectionUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = SelectorInputUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        blocks_item = TextInputUiBlock.from_dict(data, strict=True)

                        return blocks_item
                    except:  # noqa: E722
                        pass
                    return UnknownType(data)

                blocks_item = _parse_blocks_item(blocks_item_data)

                blocks.append(blocks_item)

            return blocks

        try:
            blocks = get_blocks()
        except KeyError:
            if strict:
                raise
            blocks = cast(
                Union[
                    Unset,
                    List[
                        Union[
                            ButtonUiBlock,
                            ChipUiBlock,
                            DropdownUiBlock,
                            MarkdownUiBlock,
                            SearchInputUiBlock,
                            SectionUiBlock,
                            SelectorInputUiBlock,
                            TextInputUiBlock,
                            UnknownType,
                        ]
                    ],
                ],
                UNSET,
            )

        app_canvas_create = cls(
            app_id=app_id,
            enabled=enabled,
            feature_id=feature_id,
            resource_id=resource_id,
            session_id=session_id,
            blocks=blocks,
        )

        return app_canvas_create

    @property
    def app_id(self) -> str:
        """Identifier of the app owning this canvas. For backwards compatibility, this property will be temporarily optional until the requisite time window for breaking changes in beta endpoints has passed."""
        if isinstance(self._app_id, Unset):
            raise NotPresentError(self, "app_id")
        return self._app_id

    @app_id.setter
    def app_id(self, value: str) -> None:
        self._app_id = value

    @property
    def enabled(self) -> bool:
        """Overall control for whether the canvas is interactable or not. If `false`, every block is disabled and will override the individual block's `enabled` property. If `true` or absent, the interactivity status will defer to the block's `enabled` property."""
        if isinstance(self._enabled, Unset):
            raise NotPresentError(self, "enabled")
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value

    @enabled.deleter
    def enabled(self) -> None:
        self._enabled = UNSET

    @property
    def feature_id(self) -> str:
        """ Identifier of the feature defined in Benchling App Manifest this canvas corresponds to. """
        if isinstance(self._feature_id, Unset):
            raise NotPresentError(self, "feature_id")
        return self._feature_id

    @feature_id.setter
    def feature_id(self, value: str) -> None:
        self._feature_id = value

    @feature_id.deleter
    def feature_id(self) -> None:
        self._feature_id = UNSET

    @property
    def resource_id(self) -> str:
        """ Identifier of the resource object to attach canvas to. """
        if isinstance(self._resource_id, Unset):
            raise NotPresentError(self, "resource_id")
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value: str) -> None:
        self._resource_id = value

    @resource_id.deleter
    def resource_id(self) -> None:
        self._resource_id = UNSET

    @property
    def session_id(self) -> Optional[str]:
        """Identifier of a session. If specified, app status messages from the session will be reported in the canvas."""
        if isinstance(self._session_id, Unset):
            raise NotPresentError(self, "session_id")
        return self._session_id

    @session_id.setter
    def session_id(self, value: Optional[str]) -> None:
        self._session_id = value

    @session_id.deleter
    def session_id(self) -> None:
        self._session_id = UNSET

    @property
    def blocks(
        self,
    ) -> List[
        Union[
            ButtonUiBlock,
            ChipUiBlock,
            DropdownUiBlock,
            MarkdownUiBlock,
            SearchInputUiBlock,
            SectionUiBlock,
            SelectorInputUiBlock,
            TextInputUiBlock,
            UnknownType,
        ]
    ]:
        if isinstance(self._blocks, Unset):
            raise NotPresentError(self, "blocks")
        return self._blocks

    @blocks.setter
    def blocks(
        self,
        value: List[
            Union[
                ButtonUiBlock,
                ChipUiBlock,
                DropdownUiBlock,
                MarkdownUiBlock,
                SearchInputUiBlock,
                SectionUiBlock,
                SelectorInputUiBlock,
                TextInputUiBlock,
                UnknownType,
            ]
        ],
    ) -> None:
        self._blocks = value

    @blocks.deleter
    def blocks(self) -> None:
        self._blocks = UNSET
