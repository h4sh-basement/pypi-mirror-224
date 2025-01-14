from typing import Any, Dict, Optional, Union

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_group_create_response_200 import (
    TaskmanApiV1GroupCreateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "description": str,
    "name": str,
}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, None, str] = UNSET,
    name: str,
    jira_authentication: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/group".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-authentication"] = jira_authentication

    params: Dict[str, Any] = {
        "description": description,
        "name": name,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1GroupCreateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TaskmanApiV1GroupCreateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TaskmanApiV1GroupCreateResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1GroupCreateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, None, str] = UNSET,
    name: str,
    jira_authentication: str,
) -> Response[TaskmanApiV1GroupCreateResponse200]:
    kwargs = _get_kwargs(
        client=client,
        description=description,
        name=name,
        jira_authentication=jira_authentication,
    )

    response = requests.post(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    description: Union[Unset, None, str] = UNSET,
    name: str,
    jira_authentication: str,
) -> Optional[TaskmanApiV1GroupCreateResponse200]:
    """Create a new group of tasks"""

    return sync_detailed(
        client=client,
        description=description,
        name=name,
        jira_authentication=jira_authentication,
    ).parsed
