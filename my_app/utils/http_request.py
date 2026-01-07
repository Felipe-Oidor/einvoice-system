"""
HTTP request utility module.

This module provides functions for making HTTP requests to external APIs.
"""

import requests


def post_request(url: str, data: dict, headers: dict = None):
    """
    Send a POST request to the specified URL.

    Args:
        url (str): The target URL for the POST request.
        data (dict): The data payload to send in the request body.
        headers (dict, optional): Optional HTTP headers to include.

    Returns:
        requests.Response or str: The response object if successful,
        or an error message string if an exception occurs.
    """

    try:
        # Send the POST request with a 5-second timeout
        response = requests.post(url, data=data, headers=headers, timeout=5)

        # Stop execution if the HTTP response indicates an error (for HTTP 4xx/5xx responses)
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
