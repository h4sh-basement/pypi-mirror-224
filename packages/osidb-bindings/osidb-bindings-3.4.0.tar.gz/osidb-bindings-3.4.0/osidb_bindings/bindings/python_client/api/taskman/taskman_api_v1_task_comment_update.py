from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.taskman_api_v1_task_comment_update_response_200 import (
    TaskmanApiV1TaskCommentUpdateResponse200,
)
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {
    "content": str,
}


def _get_kwargs(
    task_key: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    content: str,
    jira_authentication: str,
) -> Dict[str, Any]:
    url = "{}/taskman/api/v1/task/{task_key}/comment/{comment_id}".format(
        client.base_url,
        task_key=task_key,
        comment_id=comment_id,
    )

    headers: Dict[str, Any] = client.get_headers()

    headers["jira-authentication"] = jira_authentication

    params: Dict[str, Any] = {
        "content": content,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "params": params,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[TaskmanApiV1TaskCommentUpdateResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: TaskmanApiV1TaskCommentUpdateResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = TaskmanApiV1TaskCommentUpdateResponse200.from_dict(
                _response_200
            )

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[TaskmanApiV1TaskCommentUpdateResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    task_key: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    content: str,
    jira_authentication: str,
) -> Response[TaskmanApiV1TaskCommentUpdateResponse200]:
    kwargs = _get_kwargs(
        task_key=task_key,
        comment_id=comment_id,
        client=client,
        content=content,
        jira_authentication=jira_authentication,
    )

    response = requests.put(
        verify=client.verify_ssl,
        auth=client.auth,
        timeout=client.timeout,
        **kwargs,
    )
    response.raise_for_status()

    return _build_response(response=response)


def sync(
    task_key: str,
    comment_id: str,
    *,
    client: AuthenticatedClient,
    content: str,
    jira_authentication: str,
) -> Optional[TaskmanApiV1TaskCommentUpdateResponse200]:
    """Edit a comment in a task"""

    return sync_detailed(
        task_key=task_key,
        comment_id=comment_id,
        client=client,
        content=content,
        jira_authentication=jira_authentication,
    ).parsed
