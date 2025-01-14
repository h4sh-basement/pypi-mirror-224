import datetime
import random
from http import HTTPStatus
from time import sleep
from typing import Any, Dict, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attempt_statistics_response import AttemptStatisticsResponse
from ...models.http_error import HttpError
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset

SLEEP_TIME = 0.05
NUM_RETRIES = 3


def _get_kwargs(
    app_id: str,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/stats/app/{app_id}/attempt/".format(client.base_url, app_id=app_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat() if start_date else None

    params["startDate"] = json_start_date

    json_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat() if end_date else None

    params["endDate"] = json_end_date

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


def _parse_response(*, client: Client, response: httpx.Response) -> AttemptStatisticsResponse:
    if response.status_code == HTTPStatus.OK:
        response_200 = AttemptStatisticsResponse.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[AttemptStatisticsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[AttemptStatisticsResponse]:
    """Get App Attempt Stats

     Returns application-level statistics on message attempts

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttemptStatisticsResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
        start_date=start_date,
        end_date=end_date,
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
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
) -> AttemptStatisticsResponse:
    """Get App Attempt Stats

     Returns application-level statistics on message attempts

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttemptStatisticsResponse
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[AttemptStatisticsResponse]:
    """Get App Attempt Stats

     Returns application-level statistics on message attempts

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttemptStatisticsResponse]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
        start_date=start_date,
        end_date=end_date,
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
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
) -> AttemptStatisticsResponse:
    """Get App Attempt Stats

     Returns application-level statistics on message attempts

    Args:
        app_id (str): The app's ID or UID Example: unique-app-identifier.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttemptStatisticsResponse
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
