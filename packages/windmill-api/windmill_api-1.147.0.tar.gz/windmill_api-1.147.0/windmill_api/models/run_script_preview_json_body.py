from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.run_script_preview_json_body_args import RunScriptPreviewJsonBodyArgs
from ..models.run_script_preview_json_body_kind import RunScriptPreviewJsonBodyKind
from ..models.run_script_preview_json_body_language import RunScriptPreviewJsonBodyLanguage
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunScriptPreviewJsonBody")


@attr.s(auto_attribs=True)
class RunScriptPreviewJsonBody:
    """
    Attributes:
        args (RunScriptPreviewJsonBodyArgs):
        content (Union[Unset, str]):
        path (Union[Unset, str]):
        language (Union[Unset, RunScriptPreviewJsonBodyLanguage]):
        tag (Union[Unset, str]):
        kind (Union[Unset, RunScriptPreviewJsonBodyKind]):
    """

    args: RunScriptPreviewJsonBodyArgs
    content: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    language: Union[Unset, RunScriptPreviewJsonBodyLanguage] = UNSET
    tag: Union[Unset, str] = UNSET
    kind: Union[Unset, RunScriptPreviewJsonBodyKind] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        args = self.args.to_dict()

        content = self.content
        path = self.path
        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        tag = self.tag
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "args": args,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if path is not UNSET:
            field_dict["path"] = path
        if language is not UNSET:
            field_dict["language"] = language
        if tag is not UNSET:
            field_dict["tag"] = tag
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        args = RunScriptPreviewJsonBodyArgs.from_dict(d.pop("args"))

        content = d.pop("content", UNSET)

        path = d.pop("path", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, RunScriptPreviewJsonBodyLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = RunScriptPreviewJsonBodyLanguage(_language)

        tag = d.pop("tag", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, RunScriptPreviewJsonBodyKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = RunScriptPreviewJsonBodyKind(_kind)

        run_script_preview_json_body = cls(
            args=args,
            content=content,
            path=path,
            language=language,
            tag=tag,
            kind=kind,
        )

        run_script_preview_json_body.additional_properties = d
        return run_script_preview_json_body

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
