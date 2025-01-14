import datetime
import random
from http import HTTPStatus
from time import sleep
from typing import Any, Dict, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_error import HttpError
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_application_stats import ListResponseApplicationStats
from ...types import UNSET, Response, Unset

SLEEP_TIME = 0.05
NUM_RETRIES = 3


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime,
    until: datetime.datetime,
    limit: Union[Unset, None, int] = 50,
    iterator: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/app/stats/usage/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_since = since.isoformat()

    params["since"] = json_since

    json_until = until.isoformat()

    params["until"] = json_until

    params["limit"] = limit

    params["iterator"] = iterator

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> ListResponseApplicationStats:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListResponseApplicationStats.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        raise HttpError.init_exception(response.json(), response.status_code)
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise HttpError.init_exception(response.json(), response.status_code)
    if response.status_code == HTTPStatus.FORBIDDEN:
        raise HttpError.init_exception(response.json(), response.status_code)
    if response.status_code == HTTPStatus.NOT_FOUND:
        raise HttpError.init_exception(response.json(), response.status_code)
    if response.status_code == HTTPStatus.CONFLICT:
        raise HttpError.init_exception(response.json(), response.status_code)
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        raise HTTPValidationError.init_exception(response.json(), response.status_code)
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        raise HttpError.init_exception(response.json(), response.status_code)
    raise errors.UnexpectedStatus(response.status_code, response.content)


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListResponseApplicationStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime,
    until: datetime.datetime,
    limit: Union[Unset, None, int] = 50,
    iterator: Union[Unset, None, str] = UNSET,
) -> Response[ListResponseApplicationStats]:
    """Get App Usage Stats

     Get basic statistics for all applications.

    Args:
        since (datetime.datetime):
        until (datetime.datetime):
        limit (Union[Unset, None, int]):  Default: 50.
        iterator (Union[Unset, None, str]): The app's ID Example: app_1srOrx2ZWZBpBUvZwXKQmoEYga2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListResponseApplicationStats]
    """

    kwargs = _get_kwargs(
        client=client,
        since=since,
        until=until,
        limit=limit,
        iterator=iterator,
    )

    kwargs["headers"] = {"svix-req-id": f"{random.getrandbits(32)}", **kwargs["headers"]}

    for retry_count in range(NUM_RETRIES):
        response = httpx.request(
            verify=client.verify_ssl,
            **kwargs,
        )
        if response.status_code >= 500:
            kwargs["headers"]["svix-retry-count"] = str(retry_count)
            sleep(SLEEP_TIME * (2**retry_count))
        else:
            break

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime,
    until: datetime.datetime,
    limit: Union[Unset, None, int] = 50,
    iterator: Union[Unset, None, str] = UNSET,
) -> ListResponseApplicationStats:
    """Get App Usage Stats

     Get basic statistics for all applications.

    Args:
        since (datetime.datetime):
        until (datetime.datetime):
        limit (Union[Unset, None, int]):  Default: 50.
        iterator (Union[Unset, None, str]): The app's ID Example: app_1srOrx2ZWZBpBUvZwXKQmoEYga2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListResponseApplicationStats
    """

    return sync_detailed(
        client=client,
        since=since,
        until=until,
        limit=limit,
        iterator=iterator,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime,
    until: datetime.datetime,
    limit: Union[Unset, None, int] = 50,
    iterator: Union[Unset, None, str] = UNSET,
) -> Response[ListResponseApplicationStats]:
    """Get App Usage Stats

     Get basic statistics for all applications.

    Args:
        since (datetime.datetime):
        until (datetime.datetime):
        limit (Union[Unset, None, int]):  Default: 50.
        iterator (Union[Unset, None, str]): The app's ID Example: app_1srOrx2ZWZBpBUvZwXKQmoEYga2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListResponseApplicationStats]
    """

    kwargs = _get_kwargs(
        client=client,
        since=since,
        until=until,
        limit=limit,
        iterator=iterator,
    )

    kwargs["headers"] = {"svix-req-id": f"{random.getrandbits(32)}", **kwargs["headers"]}

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        for retry_count in range(NUM_RETRIES):
            response = await _client.request(**kwargs)
            if response.status_code >= 500:
                kwargs["headers"]["svix-retry-count"] = str(retry_count)
                sleep(SLEEP_TIME * (2**retry_count))
            else:
                break

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    since: datetime.datetime,
    until: datetime.datetime,
    limit: Union[Unset, None, int] = 50,
    iterator: Union[Unset, None, str] = UNSET,
) -> ListResponseApplicationStats:
    """Get App Usage Stats

     Get basic statistics for all applications.

    Args:
        since (datetime.datetime):
        until (datetime.datetime):
        limit (Union[Unset, None, int]):  Default: 50.
        iterator (Union[Unset, None, str]): The app's ID Example: app_1srOrx2ZWZBpBUvZwXKQmoEYga2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListResponseApplicationStats
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
            until=until,
            limit=limit,
            iterator=iterator,
        )
    ).parsed
