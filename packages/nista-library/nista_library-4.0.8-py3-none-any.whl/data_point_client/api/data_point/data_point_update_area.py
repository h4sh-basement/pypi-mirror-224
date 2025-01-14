from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.problem_details import ProblemDetails
from ...models.update_area_request import UpdateAreaRequest
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    data_point_id: str,
    area_id: str,
    *,
    client: Client,
    json_body: UpdateAreaRequest,
) -> Dict[str, Any]:
    url = "{}/DataPoint/workspace/{workspaceId}/dataPoint/{dataPointId}/area/{areaId}".format(
        client.base_url, workspaceId=workspace_id, dataPointId=data_point_id, areaId=area_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    data_point_id: str,
    area_id: str,
    *,
    client: Client,
    json_body: UpdateAreaRequest,
) -> Response[Union[Any, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_point_id (str):
        area_id (str):
        json_body (UpdateAreaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        data_point_id=data_point_id,
        area_id=area_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    data_point_id: str,
    area_id: str,
    *,
    client: Client,
    json_body: UpdateAreaRequest,
) -> Optional[Union[Any, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_point_id (str):
        area_id (str):
        json_body (UpdateAreaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        data_point_id=data_point_id,
        area_id=area_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    data_point_id: str,
    area_id: str,
    *,
    client: Client,
    json_body: UpdateAreaRequest,
) -> Response[Union[Any, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_point_id (str):
        area_id (str):
        json_body (UpdateAreaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        data_point_id=data_point_id,
        area_id=area_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    data_point_id: str,
    area_id: str,
    *,
    client: Client,
    json_body: UpdateAreaRequest,
) -> Optional[Union[Any, ProblemDetails]]:
    """
    Args:
        workspace_id (str):
        data_point_id (str):
        area_id (str):
        json_body (UpdateAreaRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            data_point_id=data_point_id,
            area_id=area_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
