from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.flow_status_module_approvers_item import FlowStatusModuleApproversItem
from ..models.flow_status_module_branch_chosen import FlowStatusModuleBranchChosen
from ..models.flow_status_module_branchall import FlowStatusModuleBranchall
from ..models.flow_status_module_iterator import FlowStatusModuleIterator
from ..models.flow_status_module_type import FlowStatusModuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowStatusModule")


@attr.s(auto_attribs=True)
class FlowStatusModule:
    """
    Attributes:
        type (FlowStatusModuleType):
        id (Union[Unset, str]):
        job (Union[Unset, str]):
        count (Union[Unset, int]):
        iterator (Union[Unset, FlowStatusModuleIterator]):
        flow_jobs (Union[Unset, List[str]]):
        branch_chosen (Union[Unset, FlowStatusModuleBranchChosen]):
        branchall (Union[Unset, FlowStatusModuleBranchall]):
        approvers (Union[Unset, List[FlowStatusModuleApproversItem]]):
    """

    type: FlowStatusModuleType
    id: Union[Unset, str] = UNSET
    job: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    iterator: Union[Unset, FlowStatusModuleIterator] = UNSET
    flow_jobs: Union[Unset, List[str]] = UNSET
    branch_chosen: Union[Unset, FlowStatusModuleBranchChosen] = UNSET
    branchall: Union[Unset, FlowStatusModuleBranchall] = UNSET
    approvers: Union[Unset, List[FlowStatusModuleApproversItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        job = self.job
        count = self.count
        iterator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iterator, Unset):
            iterator = self.iterator.to_dict()

        flow_jobs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flow_jobs, Unset):
            flow_jobs = self.flow_jobs

        branch_chosen: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branch_chosen, Unset):
            branch_chosen = self.branch_chosen.to_dict()

        branchall: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branchall, Unset):
            branchall = self.branchall.to_dict()

        approvers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approvers, Unset):
            approvers = []
            for approvers_item_data in self.approvers:
                approvers_item = approvers_item_data.to_dict()

                approvers.append(approvers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if job is not UNSET:
            field_dict["job"] = job
        if count is not UNSET:
            field_dict["count"] = count
        if iterator is not UNSET:
            field_dict["iterator"] = iterator
        if flow_jobs is not UNSET:
            field_dict["flow_jobs"] = flow_jobs
        if branch_chosen is not UNSET:
            field_dict["branch_chosen"] = branch_chosen
        if branchall is not UNSET:
            field_dict["branchall"] = branchall
        if approvers is not UNSET:
            field_dict["approvers"] = approvers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = FlowStatusModuleType(d.pop("type"))

        id = d.pop("id", UNSET)

        job = d.pop("job", UNSET)

        count = d.pop("count", UNSET)

        _iterator = d.pop("iterator", UNSET)
        iterator: Union[Unset, FlowStatusModuleIterator]
        if isinstance(_iterator, Unset):
            iterator = UNSET
        else:
            iterator = FlowStatusModuleIterator.from_dict(_iterator)

        flow_jobs = cast(List[str], d.pop("flow_jobs", UNSET))

        _branch_chosen = d.pop("branch_chosen", UNSET)
        branch_chosen: Union[Unset, FlowStatusModuleBranchChosen]
        if isinstance(_branch_chosen, Unset):
            branch_chosen = UNSET
        else:
            branch_chosen = FlowStatusModuleBranchChosen.from_dict(_branch_chosen)

        _branchall = d.pop("branchall", UNSET)
        branchall: Union[Unset, FlowStatusModuleBranchall]
        if isinstance(_branchall, Unset):
            branchall = UNSET
        else:
            branchall = FlowStatusModuleBranchall.from_dict(_branchall)

        approvers = []
        _approvers = d.pop("approvers", UNSET)
        for approvers_item_data in _approvers or []:
            approvers_item = FlowStatusModuleApproversItem.from_dict(approvers_item_data)

            approvers.append(approvers_item)

        flow_status_module = cls(
            type=type,
            id=id,
            job=job,
            count=count,
            iterator=iterator,
            flow_jobs=flow_jobs,
            branch_chosen=branch_chosen,
            branchall=branchall,
            approvers=approvers,
        )

        flow_status_module.additional_properties = d
        return flow_status_module

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
