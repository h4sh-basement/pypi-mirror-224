import datetime
import random
from http import HTTPStatus
from time import sleep
from typing import Any, Dict, List, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_error import HttpError
from ...models.http_validation_error import HTTPValidationError
from ...models.list_response_message_attempt_out import ListResponseMessageAttemptOut
from ...models.message_status import MessageStatus
from ...models.status_code_class import StatusCodeClass
from ...types import UNSET, Response, Unset

SLEEP_TIME = 0.05
NUM_RETRIES = 3


def _get_kwargs(
    app_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    iterator: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, MessageStatus] = UNSET,
    status_code_class: Union[Unset, None, StatusCodeClass] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    with_content: Union[Unset, None, bool] = True,
    event_types: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/app/{app_id}/attempt/endpoint/{endpoint_id}/".format(
        client.base_url, app_id=app_id, endpoint_id=endpoint_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["iterator"] = iterator

    json_status: Union[Unset, None, int] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    json_status_code_class: Union[Unset, None, int] = UNSET
    if not isinstance(status_code_class, Unset):
        json_status_code_class = status_code_class.value if status_code_class else None

    params["status_code_class"] = json_status_code_class

    params["channel"] = channel

    json_before: Union[Unset, None, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat() if before else None

    params["before"] = json_before

    json_after: Union[Unset, None, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat() if after else None

    params["after"] = json_after

    params["with_content"] = with_content

    json_event_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(event_types, Unset):
        if event_types is None:
            json_event_types = None
        else:
            json_event_types = event_types

    params["event_types"] = json_event_types

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


def _parse_response(*, client: Client, response: httpx.Response) -> ListResponseMessageAttemptOut:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListResponseMessageAttemptOut.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListResponseMessageAttemptOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    iterator: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, MessageStatus] = UNSET,
    status_code_class: Union[Unset, None, StatusCodeClass] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    with_content: Union[Unset, None, bool] = True,
    event_types: Union[Unset, None, List[str]] = UNSET,
) -> Response[ListResponseMessageAttemptOut]:
    """List Attempts By Endpoint

     List attempts by endpoint id

    Note that by default this endpoint is limited to retrieving 90 days' worth of data
    relative to now or, if an iterator is provided, 90 days before/after the time indicated
    by the iterator ID. If you require data beyond those time ranges, you will need to explicitly
    set the `before` or `after` parameter as appropriate.

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        endpoint_id (str): The ep's ID or UID Example: unique-ep-identifier.
        limit (Union[Unset, None, int]):
        iterator (Union[Unset, None, str]): The attempt's ID Example:
            atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2.
        status (Union[Unset, None, MessageStatus]): The sending status of the message:
            - Success = 0
            - Pending = 1
            - Fail = 2
            - Sending = 3
        status_code_class (Union[Unset, None, StatusCodeClass]): The different classes of HTTP
            status codes:
            - CodeNone = 0
            - Code1xx = 100
            - Code2xx = 200
            - Code3xx = 300
            - Code4xx = 400
            - Code5xx = 500
        channel (Union[Unset, None, str]):  Example: project_1337.
        before (Union[Unset, None, datetime.datetime]):
        after (Union[Unset, None, datetime.datetime]):
        with_content (Union[Unset, None, bool]):  Default: True.
        event_types (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListResponseMessageAttemptOut]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        endpoint_id=endpoint_id,
        client=client,
        limit=limit,
        iterator=iterator,
        status=status,
        status_code_class=status_code_class,
        channel=channel,
        before=before,
        after=after,
        with_content=with_content,
        event_types=event_types,
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
    app_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    iterator: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, MessageStatus] = UNSET,
    status_code_class: Union[Unset, None, StatusCodeClass] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    with_content: Union[Unset, None, bool] = True,
    event_types: Union[Unset, None, List[str]] = UNSET,
) -> ListResponseMessageAttemptOut:
    """List Attempts By Endpoint

     List attempts by endpoint id

    Note that by default this endpoint is limited to retrieving 90 days' worth of data
    relative to now or, if an iterator is provided, 90 days before/after the time indicated
    by the iterator ID. If you require data beyond those time ranges, you will need to explicitly
    set the `before` or `after` parameter as appropriate.

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        endpoint_id (str): The ep's ID or UID Example: unique-ep-identifier.
        limit (Union[Unset, None, int]):
        iterator (Union[Unset, None, str]): The attempt's ID Example:
            atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2.
        status (Union[Unset, None, MessageStatus]): The sending status of the message:
            - Success = 0
            - Pending = 1
            - Fail = 2
            - Sending = 3
        status_code_class (Union[Unset, None, StatusCodeClass]): The different classes of HTTP
            status codes:
            - CodeNone = 0
            - Code1xx = 100
            - Code2xx = 200
            - Code3xx = 300
            - Code4xx = 400
            - Code5xx = 500
        channel (Union[Unset, None, str]):  Example: project_1337.
        before (Union[Unset, None, datetime.datetime]):
        after (Union[Unset, None, datetime.datetime]):
        with_content (Union[Unset, None, bool]):  Default: True.
        event_types (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListResponseMessageAttemptOut
    """

    return sync_detailed(
        app_id=app_id,
        endpoint_id=endpoint_id,
        client=client,
        limit=limit,
        iterator=iterator,
        status=status,
        status_code_class=status_code_class,
        channel=channel,
        before=before,
        after=after,
        with_content=with_content,
        event_types=event_types,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    iterator: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, MessageStatus] = UNSET,
    status_code_class: Union[Unset, None, StatusCodeClass] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    with_content: Union[Unset, None, bool] = True,
    event_types: Union[Unset, None, List[str]] = UNSET,
) -> Response[ListResponseMessageAttemptOut]:
    """List Attempts By Endpoint

     List attempts by endpoint id

    Note that by default this endpoint is limited to retrieving 90 days' worth of data
    relative to now or, if an iterator is provided, 90 days before/after the time indicated
    by the iterator ID. If you require data beyond those time ranges, you will need to explicitly
    set the `before` or `after` parameter as appropriate.

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        endpoint_id (str): The ep's ID or UID Example: unique-ep-identifier.
        limit (Union[Unset, None, int]):
        iterator (Union[Unset, None, str]): The attempt's ID Example:
            atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2.
        status (Union[Unset, None, MessageStatus]): The sending status of the message:
            - Success = 0
            - Pending = 1
            - Fail = 2
            - Sending = 3
        status_code_class (Union[Unset, None, StatusCodeClass]): The different classes of HTTP
            status codes:
            - CodeNone = 0
            - Code1xx = 100
            - Code2xx = 200
            - Code3xx = 300
            - Code4xx = 400
            - Code5xx = 500
        channel (Union[Unset, None, str]):  Example: project_1337.
        before (Union[Unset, None, datetime.datetime]):
        after (Union[Unset, None, datetime.datetime]):
        with_content (Union[Unset, None, bool]):  Default: True.
        event_types (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListResponseMessageAttemptOut]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        endpoint_id=endpoint_id,
        client=client,
        limit=limit,
        iterator=iterator,
        status=status,
        status_code_class=status_code_class,
        channel=channel,
        before=before,
        after=after,
        with_content=with_content,
        event_types=event_types,
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
    app_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = UNSET,
    iterator: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, MessageStatus] = UNSET,
    status_code_class: Union[Unset, None, StatusCodeClass] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, datetime.datetime] = UNSET,
    after: Union[Unset, None, datetime.datetime] = UNSET,
    with_content: Union[Unset, None, bool] = True,
    event_types: Union[Unset, None, List[str]] = UNSET,
) -> ListResponseMessageAttemptOut:
    """List Attempts By Endpoint

     List attempts by endpoint id

    Note that by default this endpoint is limited to retrieving 90 days' worth of data
    relative to now or, if an iterator is provided, 90 days before/after the time indicated
    by the iterator ID. If you require data beyond those time ranges, you will need to explicitly
    set the `before` or `after` parameter as appropriate.

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        endpoint_id (str): The ep's ID or UID Example: unique-ep-identifier.
        limit (Union[Unset, None, int]):
        iterator (Union[Unset, None, str]): The attempt's ID Example:
            atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2.
        status (Union[Unset, None, MessageStatus]): The sending status of the message:
            - Success = 0
            - Pending = 1
            - Fail = 2
            - Sending = 3
        status_code_class (Union[Unset, None, StatusCodeClass]): The different classes of HTTP
            status codes:
            - CodeNone = 0
            - Code1xx = 100
            - Code2xx = 200
            - Code3xx = 300
            - Code4xx = 400
            - Code5xx = 500
        channel (Union[Unset, None, str]):  Example: project_1337.
        before (Union[Unset, None, datetime.datetime]):
        after (Union[Unset, None, datetime.datetime]):
        with_content (Union[Unset, None, bool]):  Default: True.
        event_types (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListResponseMessageAttemptOut
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            endpoint_id=endpoint_id,
            client=client,
            limit=limit,
            iterator=iterator,
            status=status,
            status_code_class=status_code_class,
            channel=channel,
            before=before,
            after=after,
            with_content=with_content,
            event_types=event_types,
        )
    ).parsed
