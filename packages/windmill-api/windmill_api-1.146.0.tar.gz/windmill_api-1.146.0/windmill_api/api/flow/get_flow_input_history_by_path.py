from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.get_flow_input_history_by_path_response_200_item import GetFlowInputHistoryByPathResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    path: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/flows/input_history/p/{path}".format(client.base_url, workspace=workspace, path=path)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[GetFlowInputHistoryByPathResponse200Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetFlowInputHistoryByPathResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[GetFlowInputHistoryByPathResponse200Item]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    path: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Response[List[GetFlowInputHistoryByPathResponse200Item]]:
    """list inputs for previous completed flow jobs

    Args:
        workspace (str):
        path (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Returns:
        Response[List[GetFlowInputHistoryByPathResponse200Item]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        path=path,
        client=client,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    path: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Optional[List[GetFlowInputHistoryByPathResponse200Item]]:
    """list inputs for previous completed flow jobs

    Args:
        workspace (str):
        path (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Returns:
        Response[List[GetFlowInputHistoryByPathResponse200Item]]
    """

    return sync_detailed(
        workspace=workspace,
        path=path,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    path: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Response[List[GetFlowInputHistoryByPathResponse200Item]]:
    """list inputs for previous completed flow jobs

    Args:
        workspace (str):
        path (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Returns:
        Response[List[GetFlowInputHistoryByPathResponse200Item]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        path=path,
        client=client,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    path: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
) -> Optional[List[GetFlowInputHistoryByPathResponse200Item]]:
    """list inputs for previous completed flow jobs

    Args:
        workspace (str):
        path (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):

    Returns:
        Response[List[GetFlowInputHistoryByPathResponse200Item]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            path=path,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
