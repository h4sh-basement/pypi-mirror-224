import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.app_with_last_version_w_draft_execution_mode import AppWithLastVersionWDraftExecutionMode
from ..models.app_with_last_version_w_draft_extra_perms import AppWithLastVersionWDraftExtraPerms
from ..models.app_with_last_version_w_draft_policy import AppWithLastVersionWDraftPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="AppWithLastVersionWDraft")


@attr.s(auto_attribs=True)
class AppWithLastVersionWDraft:
    """
    Attributes:
        id (int):
        workspace_id (str):
        path (str):
        summary (str):
        versions (List[int]):
        created_by (str):
        created_at (datetime.datetime):
        value (Any):
        policy (AppWithLastVersionWDraftPolicy):
        execution_mode (AppWithLastVersionWDraftExecutionMode):
        extra_perms (AppWithLastVersionWDraftExtraPerms):
        draft_only (Union[Unset, bool]):
        draft (Union[Unset, Any]):
    """

    id: int
    workspace_id: str
    path: str
    summary: str
    versions: List[int]
    created_by: str
    created_at: datetime.datetime
    value: Any
    policy: AppWithLastVersionWDraftPolicy
    execution_mode: AppWithLastVersionWDraftExecutionMode
    extra_perms: AppWithLastVersionWDraftExtraPerms
    draft_only: Union[Unset, bool] = UNSET
    draft: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        workspace_id = self.workspace_id
        path = self.path
        summary = self.summary
        versions = self.versions

        created_by = self.created_by
        created_at = self.created_at.isoformat()

        value = self.value
        policy = self.policy.to_dict()

        execution_mode = self.execution_mode.value

        extra_perms = self.extra_perms.to_dict()

        draft_only = self.draft_only
        draft = self.draft

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace_id": workspace_id,
                "path": path,
                "summary": summary,
                "versions": versions,
                "created_by": created_by,
                "created_at": created_at,
                "value": value,
                "policy": policy,
                "execution_mode": execution_mode,
                "extra_perms": extra_perms,
            }
        )
        if draft_only is not UNSET:
            field_dict["draft_only"] = draft_only
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        workspace_id = d.pop("workspace_id")

        path = d.pop("path")

        summary = d.pop("summary")

        versions = cast(List[int], d.pop("versions"))

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))

        value = d.pop("value")

        policy = AppWithLastVersionWDraftPolicy.from_dict(d.pop("policy"))

        execution_mode = AppWithLastVersionWDraftExecutionMode(d.pop("execution_mode"))

        extra_perms = AppWithLastVersionWDraftExtraPerms.from_dict(d.pop("extra_perms"))

        draft_only = d.pop("draft_only", UNSET)

        draft = d.pop("draft", UNSET)

        app_with_last_version_w_draft = cls(
            id=id,
            workspace_id=workspace_id,
            path=path,
            summary=summary,
            versions=versions,
            created_by=created_by,
            created_at=created_at,
            value=value,
            policy=policy,
            execution_mode=execution_mode,
            extra_perms=extra_perms,
            draft_only=draft_only,
            draft=draft,
        )

        app_with_last_version_w_draft.additional_properties = d
        return app_with_last_version_w_draft

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
