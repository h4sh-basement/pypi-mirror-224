from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_deploy_to_response_200 import GetDeployToResponse200
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/workspaces/get_deploy_to".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetDeployToResponse200]:
    if response.status_code == 200:
        response_200 = GetDeployToResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetDeployToResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[GetDeployToResponse200]:
    """get deploy to

    Args:
        workspace (str):

    Returns:
        Response[GetDeployToResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    client: Client,
) -> Optional[GetDeployToResponse200]:
    """get deploy to

    Args:
        workspace (str):

    Returns:
        Response[GetDeployToResponse200]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[GetDeployToResponse200]:
    """get deploy to

    Args:
        workspace (str):

    Returns:
        Response[GetDeployToResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: Client,
) -> Optional[GetDeployToResponse200]:
    """get deploy to

    Args:
        workspace (str):

    Returns:
        Response[GetDeployToResponse200]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
