"""
HTTP Requests Module

This module handles requests to an API
"""

import requests
from typing import Optional, Literal, Dict, Any


def http_requests(
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
    url: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, Any]] = None,
    timeout: Optional[int] = 5,
) -> dict[str, Any]:
    """
    Send an HTTP request to an API and return the response as a dictionary.

    Args:
        - method (str): HTTP method ("GET", "POST", "PUT", "PATCH", "DELETE").
        - url (str): Endpoint URL.
        - params (dict, optional): Query parameters to add to the URL.
        - data (dict, optional): Payload for POST/PUT/PATCH requests.
        - headers (dict, optional): HTTP headers for the request.
        - timeout (int, optional): Time in seconds to wait for a response (default 5).

    Returns:
        - dict: Response JSON content.
    """
    response = requests.request(
        method=method,
        url=url,
        params=params,
        data=data,
        headers=headers,
        timeout=timeout,
    )

    if response.status_code == 200:
        data = response.json()
    return data
