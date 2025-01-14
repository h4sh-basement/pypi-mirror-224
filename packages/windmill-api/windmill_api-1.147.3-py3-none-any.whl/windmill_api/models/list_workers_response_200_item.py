import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWorkersResponse200Item")


@attr.s(auto_attribs=True)
class ListWorkersResponse200Item:
    """
    Attributes:
        worker (str):
        worker_instance (str):
        started_at (datetime.datetime):
        ip (str):
        jobs_executed (int):
        last_ping (Union[Unset, float]):
        custom_tags (Union[Unset, List[str]]):
    """

    worker: str
    worker_instance: str
    started_at: datetime.datetime
    ip: str
    jobs_executed: int
    last_ping: Union[Unset, float] = UNSET
    custom_tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worker = self.worker
        worker_instance = self.worker_instance
        started_at = self.started_at.isoformat()

        ip = self.ip
        jobs_executed = self.jobs_executed
        last_ping = self.last_ping
        custom_tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.custom_tags, Unset):
            custom_tags = self.custom_tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worker": worker,
                "worker_instance": worker_instance,
                "started_at": started_at,
                "ip": ip,
                "jobs_executed": jobs_executed,
            }
        )
        if last_ping is not UNSET:
            field_dict["last_ping"] = last_ping
        if custom_tags is not UNSET:
            field_dict["custom_tags"] = custom_tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worker = d.pop("worker")

        worker_instance = d.pop("worker_instance")

        started_at = isoparse(d.pop("started_at"))

        ip = d.pop("ip")

        jobs_executed = d.pop("jobs_executed")

        last_ping = d.pop("last_ping", UNSET)

        custom_tags = cast(List[str], d.pop("custom_tags", UNSET))

        list_workers_response_200_item = cls(
            worker=worker,
            worker_instance=worker_instance,
            started_at=started_at,
            ip=ip,
            jobs_executed=jobs_executed,
            last_ping=last_ping,
            custom_tags=custom_tags,
        )

        list_workers_response_200_item.additional_properties = d
        return list_workers_response_200_item

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
