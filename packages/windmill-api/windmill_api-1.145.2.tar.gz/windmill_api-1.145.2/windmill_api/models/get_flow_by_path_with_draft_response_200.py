from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_flow_by_path_with_draft_response_200_draft import GetFlowByPathWithDraftResponse200Draft
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFlowByPathWithDraftResponse200")


@attr.s(auto_attribs=True)
class GetFlowByPathWithDraftResponse200:
    """
    Attributes:
        draft (Union[Unset, GetFlowByPathWithDraftResponse200Draft]):
    """

    draft: Union[Unset, GetFlowByPathWithDraftResponse200Draft] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        draft: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _draft = d.pop("draft", UNSET)
        draft: Union[Unset, GetFlowByPathWithDraftResponse200Draft]
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = GetFlowByPathWithDraftResponse200Draft.from_dict(_draft)

        get_flow_by_path_with_draft_response_200 = cls(
            draft=draft,
        )

        get_flow_by_path_with_draft_response_200.additional_properties = d
        return get_flow_by_path_with_draft_response_200

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
