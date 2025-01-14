from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GetCompletedJobResultMaybeResponse200")


@attr.s(auto_attribs=True)
class GetCompletedJobResultMaybeResponse200:
    """
    Attributes:
        completed (bool):
        result (Any):
    """

    completed: bool
    result: Any
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completed = self.completed
        result = self.result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completed": completed,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        completed = d.pop("completed")

        result = d.pop("result")

        get_completed_job_result_maybe_response_200 = cls(
            completed=completed,
            result=result,
        )

        get_completed_job_result_maybe_response_200.additional_properties = d
        return get_completed_job_result_maybe_response_200

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
