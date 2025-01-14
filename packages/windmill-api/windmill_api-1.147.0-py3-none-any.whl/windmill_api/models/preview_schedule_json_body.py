from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PreviewScheduleJsonBody")


@attr.s(auto_attribs=True)
class PreviewScheduleJsonBody:
    """
    Attributes:
        schedule (str):
        timezone (str):
    """

    schedule: str
    timezone: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule = self.schedule
        timezone = self.timezone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule": schedule,
                "timezone": timezone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schedule = d.pop("schedule")

        timezone = d.pop("timezone")

        preview_schedule_json_body = cls(
            schedule=schedule,
            timezone=timezone,
        )

        preview_schedule_json_body.additional_properties = d
        return preview_schedule_json_body

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
