import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.get_public_app_by_secret_response_200_execution_mode import GetPublicAppBySecretResponse200ExecutionMode
from ..models.get_public_app_by_secret_response_200_extra_perms import GetPublicAppBySecretResponse200ExtraPerms
from ..models.get_public_app_by_secret_response_200_policy import GetPublicAppBySecretResponse200Policy

T = TypeVar("T", bound="GetPublicAppBySecretResponse200")


@attr.s(auto_attribs=True)
class GetPublicAppBySecretResponse200:
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
        policy (GetPublicAppBySecretResponse200Policy):
        execution_mode (GetPublicAppBySecretResponse200ExecutionMode):
        extra_perms (GetPublicAppBySecretResponse200ExtraPerms):
    """

    id: int
    workspace_id: str
    path: str
    summary: str
    versions: List[int]
    created_by: str
    created_at: datetime.datetime
    value: Any
    policy: GetPublicAppBySecretResponse200Policy
    execution_mode: GetPublicAppBySecretResponse200ExecutionMode
    extra_perms: GetPublicAppBySecretResponse200ExtraPerms
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

        policy = GetPublicAppBySecretResponse200Policy.from_dict(d.pop("policy"))

        execution_mode = GetPublicAppBySecretResponse200ExecutionMode(d.pop("execution_mode"))

        extra_perms = GetPublicAppBySecretResponse200ExtraPerms.from_dict(d.pop("extra_perms"))

        get_public_app_by_secret_response_200 = cls(
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
        )

        get_public_app_by_secret_response_200.additional_properties = d
        return get_public_app_by_secret_response_200

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
