from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.delete_completed_job_response_200_raw_flow_failure_module_mock import (
    DeleteCompletedJobResponse200RawFlowFailureModuleMock,
)
from ..models.delete_completed_job_response_200_raw_flow_failure_module_retry import (
    DeleteCompletedJobResponse200RawFlowFailureModuleRetry,
)
from ..models.delete_completed_job_response_200_raw_flow_failure_module_sleep_type_0 import (
    DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0,
)
from ..models.delete_completed_job_response_200_raw_flow_failure_module_sleep_type_1 import (
    DeleteCompletedJobResponse200RawFlowFailureModuleSleepType1,
)
from ..models.delete_completed_job_response_200_raw_flow_failure_module_stop_after_if import (
    DeleteCompletedJobResponse200RawFlowFailureModuleStopAfterIf,
)
from ..models.delete_completed_job_response_200_raw_flow_failure_module_suspend import (
    DeleteCompletedJobResponse200RawFlowFailureModuleSuspend,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCompletedJobResponse200RawFlowFailureModule")


@attr.s(auto_attribs=True)
class DeleteCompletedJobResponse200RawFlowFailureModule:
    """
    Attributes:
        id (str):
        value (Any):
        stop_after_if (Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleStopAfterIf]):
        sleep (Union[DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0,
            DeleteCompletedJobResponse200RawFlowFailureModuleSleepType1, Unset]):
        cache_ttl (Union[Unset, float]):
        timeout (Union[Unset, float]):
        summary (Union[Unset, str]):
        mock (Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleMock]):
        suspend (Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleSuspend]):
        retry (Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleRetry]):
    """

    id: str
    value: Any
    stop_after_if: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleStopAfterIf] = UNSET
    sleep: Union[
        DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0,
        DeleteCompletedJobResponse200RawFlowFailureModuleSleepType1,
        Unset,
    ] = UNSET
    cache_ttl: Union[Unset, float] = UNSET
    timeout: Union[Unset, float] = UNSET
    summary: Union[Unset, str] = UNSET
    mock: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleMock] = UNSET
    suspend: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleSuspend] = UNSET
    retry: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleRetry] = UNSET
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

        elif isinstance(self.sleep, DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0):
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
        stop_after_if: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleStopAfterIf]
        if isinstance(_stop_after_if, Unset):
            stop_after_if = UNSET
        else:
            stop_after_if = DeleteCompletedJobResponse200RawFlowFailureModuleStopAfterIf.from_dict(_stop_after_if)

        def _parse_sleep(
            data: object,
        ) -> Union[
            DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0,
            DeleteCompletedJobResponse200RawFlowFailureModuleSleepType1,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _sleep_type_0 = data
                sleep_type_0: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0]
                if isinstance(_sleep_type_0, Unset):
                    sleep_type_0 = UNSET
                else:
                    sleep_type_0 = DeleteCompletedJobResponse200RawFlowFailureModuleSleepType0.from_dict(_sleep_type_0)

                return sleep_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _sleep_type_1 = data
            sleep_type_1: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleSleepType1]
            if isinstance(_sleep_type_1, Unset):
                sleep_type_1 = UNSET
            else:
                sleep_type_1 = DeleteCompletedJobResponse200RawFlowFailureModuleSleepType1.from_dict(_sleep_type_1)

            return sleep_type_1

        sleep = _parse_sleep(d.pop("sleep", UNSET))

        cache_ttl = d.pop("cache_ttl", UNSET)

        timeout = d.pop("timeout", UNSET)

        summary = d.pop("summary", UNSET)

        _mock = d.pop("mock", UNSET)
        mock: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleMock]
        if isinstance(_mock, Unset):
            mock = UNSET
        else:
            mock = DeleteCompletedJobResponse200RawFlowFailureModuleMock.from_dict(_mock)

        _suspend = d.pop("suspend", UNSET)
        suspend: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleSuspend]
        if isinstance(_suspend, Unset):
            suspend = UNSET
        else:
            suspend = DeleteCompletedJobResponse200RawFlowFailureModuleSuspend.from_dict(_suspend)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, DeleteCompletedJobResponse200RawFlowFailureModuleRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = DeleteCompletedJobResponse200RawFlowFailureModuleRetry.from_dict(_retry)

        delete_completed_job_response_200_raw_flow_failure_module = cls(
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

        delete_completed_job_response_200_raw_flow_failure_module.additional_properties = d
        return delete_completed_job_response_200_raw_flow_failure_module

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
