"""
HTTP request utility module.

This module provides functions for making HTTP requests to external APIs.
"""

import requests
from typing import Literal, Optional


def http_request(
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
    url: str,
    *,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    json: Optional[dict] = None,
    headers: Optional[dict] = None,
    timeout: int = 5,
):
    """
    Generic HTTP request with error handling.

    Returns:
        requests.Reponse if successful, otherwise a string describing the error.
    """

    try:
        response = requests.request(
            method,
            url,
            params=params,
            data=data,
            json=json,
            headers=headers,
            timeout=timeout,
        )

        response.raise_for_status()

    # Handle HTTP error response (4xx or 5xx)
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error: {http_err}"

    # Handle network-related errors (e.g., DNS failure, refused connection)
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error: {conn_err}"

    # Handle request timeout
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error: {timeout_err}"

    # Handle any other requests exception
    except requests.exceptions.RequestException as req_err:
        return f"Unexpected error: {req_err}"

    # If no exceptions, return the successful response
    else:
        return response
