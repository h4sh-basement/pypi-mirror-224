from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_completed_job_response_200_flow_status_failure_module import (
    GetCompletedJobResponse200FlowStatusFailureModule,
)
from ..models.get_completed_job_response_200_flow_status_modules_item import (
    GetCompletedJobResponse200FlowStatusModulesItem,
)
from ..models.get_completed_job_response_200_flow_status_retry import GetCompletedJobResponse200FlowStatusRetry
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCompletedJobResponse200FlowStatus")


@attr.s(auto_attribs=True)
class GetCompletedJobResponse200FlowStatus:
    """
    Attributes:
        step (int):
        modules (List[GetCompletedJobResponse200FlowStatusModulesItem]):
        failure_module (GetCompletedJobResponse200FlowStatusFailureModule):
        retry (Union[Unset, GetCompletedJobResponse200FlowStatusRetry]):
    """

    step: int
    modules: List[GetCompletedJobResponse200FlowStatusModulesItem]
    failure_module: GetCompletedJobResponse200FlowStatusFailureModule
    retry: Union[Unset, GetCompletedJobResponse200FlowStatusRetry] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step = self.step
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        failure_module = self.failure_module.to_dict()

        retry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "modules": modules,
                "failure_module": failure_module,
            }
        )
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        step = d.pop("step")

        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = GetCompletedJobResponse200FlowStatusModulesItem.from_dict(modules_item_data)

            modules.append(modules_item)

        failure_module = GetCompletedJobResponse200FlowStatusFailureModule.from_dict(d.pop("failure_module"))

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, GetCompletedJobResponse200FlowStatusRetry]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = GetCompletedJobResponse200FlowStatusRetry.from_dict(_retry)

        get_completed_job_response_200_flow_status = cls(
            step=step,
            modules=modules,
            failure_module=failure_module,
            retry=retry,
        )

        get_completed_job_response_200_flow_status.additional_properties = d
        return get_completed_job_response_200_flow_status

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
