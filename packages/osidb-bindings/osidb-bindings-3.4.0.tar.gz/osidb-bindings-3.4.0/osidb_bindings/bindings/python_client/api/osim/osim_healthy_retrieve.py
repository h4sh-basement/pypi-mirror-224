from typing import Any, Dict, Optional

import requests

from ...client import AuthenticatedClient
from ...models.osim_healthy_retrieve_response_200 import OsimHealthyRetrieveResponse200
from ...types import UNSET, Response, Unset

QUERY_PARAMS = {}


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/osim/healthy".format(
        client.base_url,
    )

    headers: Dict[str, Any] = client.get_headers()

    return {
        "url": url,
        "headers": headers,
    }


def _parse_response(
    *, response: requests.Response
) -> Optional[OsimHealthyRetrieveResponse200]:
    if response.status_code == 200:
        _response_200 = response.json()
        response_200: OsimHealthyRetrieveResponse200
        if isinstance(_response_200, Unset):
            response_200 = UNSET
        else:
            response_200 = OsimHealthyRetrieveResponse200.from_dict(_response_200)

        return response_200
    return None


def _build_response(
    *, response: requests.Response
) -> Response[OsimHealthyRetrieveResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OsimHealthyRetrieveResponse200]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = requests.get(
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
) -> Optional[OsimHealthyRetrieveResponse200]:
    """unauthenticated health check API endpoint"""

    return sync_detailed(
        client=client,
    ).parsed
