from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditOpenaiResourcePathJsonBody")


@attr.s(auto_attribs=True)
class EditOpenaiResourcePathJsonBody:
    """
    Attributes:
        openai_resource_path (Union[Unset, str]):
    """

    openai_resource_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        openai_resource_path = self.openai_resource_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if openai_resource_path is not UNSET:
            field_dict["openai_resource_path"] = openai_resource_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        openai_resource_path = d.pop("openai_resource_path", UNSET)

        edit_openai_resource_path_json_body = cls(
            openai_resource_path=openai_resource_path,
        )

        edit_openai_resource_path_json_body.additional_properties = d
        return edit_openai_resource_path_json_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
