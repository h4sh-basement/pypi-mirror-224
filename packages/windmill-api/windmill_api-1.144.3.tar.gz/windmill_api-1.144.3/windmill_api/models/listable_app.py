import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.listable_app_execution_mode import ListableAppExecutionMode
from ..models.listable_app_extra_perms import ListableAppExtraPerms
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListableApp")


@attr.s(auto_attribs=True)
class ListableApp:
    """
    Attributes:
        id (int):
        workspace_id (str):
        path (str):
        summary (str):
        version (int):
        extra_perms (ListableAppExtraPerms):
        edited_at (datetime.datetime):
        execution_mode (ListableAppExecutionMode):
        starred (Union[Unset, bool]):
    """

    id: int
    workspace_id: str
    path: str
    summary: str
    version: int
    extra_perms: ListableAppExtraPerms
    edited_at: datetime.datetime
    execution_mode: ListableAppExecutionMode
    starred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        workspace_id = self.workspace_id
        path = self.path
        summary = self.summary
        version = self.version
        extra_perms = self.extra_perms.to_dict()

        edited_at = self.edited_at.isoformat()

        execution_mode = self.execution_mode.value

        starred = self.starred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "path": path,
                "summary": summary,
                "version": version,
                "extra_perms": extra_perms,
                "edited_at": edited_at,
                "execution_mode": execution_mode,
            }
        )
        if starred is not UNSET:
            field_dict["starred"] = starred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        path = d.pop("path")

        summary = d.pop("summary")

        version = d.pop("version")

        extra_perms = ListableAppExtraPerms.from_dict(d.pop("extra_perms"))

        edited_at = isoparse(d.pop("edited_at"))

        execution_mode = ListableAppExecutionMode(d.pop("execution_mode"))

        starred = d.pop("starred", UNSET)

        listable_app = cls(
            id=id,
            workspace_id=workspace_id,
            path=path,
            summary=summary,
            version=version,
            extra_perms=extra_perms,
            edited_at=edited_at,
            execution_mode=execution_mode,
            starred=starred,
        )

        listable_app.additional_properties = d
        return listable_app

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
