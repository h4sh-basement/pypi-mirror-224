import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.get_schedule_response_200_args import GetScheduleResponse200Args
from ..models.get_schedule_response_200_extra_perms import GetScheduleResponse200ExtraPerms
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScheduleResponse200")


@attr.s(auto_attribs=True)
class GetScheduleResponse200:
    """
    Attributes:
        path (str):
        edited_by (str):
        edited_at (datetime.datetime):
        schedule (str):
        timezone (str):
        enabled (bool):
        script_path (str):
        is_flow (bool):
        extra_perms (GetScheduleResponse200ExtraPerms):
        email (str):
        args (Union[Unset, GetScheduleResponse200Args]):
        error (Union[Unset, str]):
        on_failure (Union[Unset, str]):
    """

    path: str
    edited_by: str
    edited_at: datetime.datetime
    schedule: str
    timezone: str
    enabled: bool
    script_path: str
    is_flow: bool
    extra_perms: GetScheduleResponse200ExtraPerms
    email: str
    args: Union[Unset, GetScheduleResponse200Args] = UNSET
    error: Union[Unset, str] = UNSET
    on_failure: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        edited_by = self.edited_by
        edited_at = self.edited_at.isoformat()

        schedule = self.schedule
        timezone = self.timezone
        enabled = self.enabled
        script_path = self.script_path
        is_flow = self.is_flow
        extra_perms = self.extra_perms.to_dict()

        email = self.email
        args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        error = self.error
        on_failure = self.on_failure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "edited_by": edited_by,
                "edited_at": edited_at,
                "schedule": schedule,
                "timezone": timezone,
                "enabled": enabled,
                "script_path": script_path,
                "is_flow": is_flow,
                "extra_perms": extra_perms,
                "email": email,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if error is not UNSET:
            field_dict["error"] = error
        if on_failure is not UNSET:
            field_dict["on_failure"] = on_failure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        edited_by = d.pop("edited_by")

        edited_at = isoparse(d.pop("edited_at"))

        schedule = d.pop("schedule")

        timezone = d.pop("timezone")

        enabled = d.pop("enabled")

        script_path = d.pop("script_path")

        is_flow = d.pop("is_flow")

        extra_perms = GetScheduleResponse200ExtraPerms.from_dict(d.pop("extra_perms"))

        email = d.pop("email")

        _args = d.pop("args", UNSET)
        args: Union[Unset, GetScheduleResponse200Args]
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = GetScheduleResponse200Args.from_dict(_args)

        error = d.pop("error", UNSET)

        on_failure = d.pop("on_failure", UNSET)

        get_schedule_response_200 = cls(
            path=path,
            edited_by=edited_by,
            edited_at=edited_at,
            schedule=schedule,
            timezone=timezone,
            enabled=enabled,
            script_path=script_path,
            is_flow=is_flow,
            extra_perms=extra_perms,
            email=email,
            args=args,
            error=error,
            on_failure=on_failure,
        )

        get_schedule_response_200.additional_properties = d
        return get_schedule_response_200

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
