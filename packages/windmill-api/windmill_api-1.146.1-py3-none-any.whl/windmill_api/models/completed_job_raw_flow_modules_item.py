from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.completed_job_raw_flow_modules_item_mock import CompletedJobRawFlowModulesItemMock
from ..models.completed_job_raw_flow_modules_item_retry import CompletedJobRawFlowModulesItemRetry
from ..models.completed_job_raw_flow_modules_item_sleep_type_0 import CompletedJobRawFlowModulesItemSleepType0
from ..models.completed_job_raw_flow_modules_item_sleep_type_1 import CompletedJobRawFlowModulesItemSleepType1
from ..models.completed_job_raw_flow_modules_item_stop_after_if import CompletedJobRawFlowModulesItemStopAfterIf
from ..models.completed_job_raw_flow_modules_item_suspend import CompletedJobRawFlowModulesItemSuspend
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompletedJobRawFlowModulesItem")


@attr.s(auto_attribs=True)
class CompletedJobRawFlowModulesItem:
    """
    Attributes:
        id (str):
        value (Any):
        stop_after_if (Union[Unset, CompletedJobRawFlowModulesItemStopAfterIf]):
        sleep (Union[CompletedJobRawFlowModulesItemSleepType0, CompletedJobRawFlowModulesItemSleepType1, Unset]):
        cache_ttl (Union[Unset, float]):
        timeout (Union[Unset, float]):
        summary (Union[Unset, str]):
        mock (Union[Unset, CompletedJobRawFlowModulesItemMock]):
        suspend (Union[Unset, CompletedJobRawFlowModulesItemSuspend]):
        retry (Union[Unset, CompletedJobRawFlowModulesItemRetry]):
    """

    id: str
    value: Any
    stop_after_if: Union[Unset, CompletedJobRawFlowModulesItemStopAfterIf] = UNSET
    sleep: Union[CompletedJobRawFlowModulesItemSleepType0, CompletedJobRawFlowModulesItemSleepType1, Unset] = UNSET
    cache_ttl: Union[Unset, float] = UNSET
    timeout: Union[Unset, float] = UNSET
    summary: Union[Unset, str] = UNSET
    mock: Union[Unset, CompletedJobRawFlowModulesItemMock] = UNSET
    suspend: Union[Unset, CompletedJobRawFlowModulesItemSuspend] = UNSET
    retry: Union[Unset, CompletedJobRawFlowModulesItemRetry] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        stop_after_if: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_after_if, Unset):
            stop_after_if = self.stop_after_if.to_dict()

        sleep: Union[Dict[str, Any], Unset]
        if isinstance(self.sleep, Unset):
            sleep = UNSET

        elif isinstance(self.sleep, CompletedJobRawFlowModulesItemSleepType0):
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        else:
            sleep = UNSET
            if not isinstance(self.sleep, Unset):
                sleep = self.sleep.to_dict()

        cache_ttl = self.cache_ttl
        timeout = self.timeout
        summary = self.summary
        mock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mock, Unset):
            mock = self.mock.to_dict()

        suspend: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suspend, Unset):
            suspend = self.suspend.to_dict()

        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
            }
        )
        if stop_after_if is not UNSET:
            field_dict["stop_after_if"] = stop_after_if
        if sleep is not UNSET:
            field_dict["sleep"] = sleep
        if cache_ttl is not UNSET:
            field_dict["cache_ttl"] = cache_ttl
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if summary is not UNSET:
            field_dict["summary"] = summary
        if mock is not UNSET:
            field_dict["mock"] = mock
        if suspend is not UNSET:
            field_dict["suspend"] = suspend
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        value = d.pop("value")

        _stop_after_if = d.pop("stop_after_if", UNSET)
        stop_after_if: Union[Unset, CompletedJobRawFlowModulesItemStopAfterIf]
        if isinstance(_stop_after_if, Unset):
            stop_after_if = UNSET
        else:
            stop_after_if = CompletedJobRawFlowModulesItemStopAfterIf.from_dict(_stop_after_if)

        def _parse_sleep(
            data: object,
        ) -> Union[CompletedJobRawFlowModulesItemSleepType0, CompletedJobRawFlowModulesItemSleepType1, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sleep_type_0 = data
                sleep_type_0: Union[Unset, CompletedJobRawFlowModulesItemSleepType0]
                if isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = UNSET
                else:
                    sleep_type_0 = CompletedJobRawFlowModulesItemSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _sleep_type_1 = data
            sleep_type_1: Union[Unset, CompletedJobRawFlowModulesItemSleepType1]
            if isinstance(_sleep_type_1, Unset):
                sleep_type_1 = UNSET
            else:
                sleep_type_1 = CompletedJobRawFlowModulesItemSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        cache_ttl = d.pop("cache_ttl", UNSET)

        timeout = d.pop("timeout", UNSET)

        summary = d.pop("summary", UNSET)

        _mock = d.pop("mock", UNSET)
        mock: Union[Unset, CompletedJobRawFlowModulesItemMock]
        if isinstance(_mock, Unset):
            mock = UNSET
        else:
            mock = CompletedJobRawFlowModulesItemMock.from_dict(_mock)

        _suspend = d.pop("suspend", UNSET)
        suspend: Union[Unset, CompletedJobRawFlowModulesItemSuspend]
        if isinstance(_suspend, Unset):
            suspend = UNSET
        else:
            suspend = CompletedJobRawFlowModulesItemSuspend.from_dict(_suspend)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, CompletedJobRawFlowModulesItemRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = CompletedJobRawFlowModulesItemRetry.from_dict(_retry)

        completed_job_raw_flow_modules_item = cls(
            id=id,
            value=value,
            stop_after_if=stop_after_if,
            sleep=sleep,
            cache_ttl=cache_ttl,
            timeout=timeout,
            summary=summary,
            mock=mock,
            suspend=suspend,
            retry=retry,
        )

        completed_job_raw_flow_modules_item.additional_properties = d
        return completed_job_raw_flow_modules_item

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
