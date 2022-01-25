import logging

import requests
from enum import Enum

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    for handler in logging.getLogger().handlers:
        logger.addHandler(handler)

_Codes = {
    200: "OK",

    401: "UNAUTHORIZED",
    400: "BAD REQUEST",
    403: "FORBIDDEN",
    404: "NOT FOUND",
    405: "METHOD NOT ALLOWED",

    500: "INTERNAL SERVER ERROR",
}


class _Methods(Enum):
    GET = 1
    HEAD = 2
    POST = 3
    PUT = 4
    DELETE = 5
    CONNECT = 6
    OPTIONS = 7
    TRACE = 8


def _Send_Request(
        _=None,
        method: _Methods = None,
        url=None,
        data=None,
        json=None,
        params=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None,
        supress=False,
):
    logger.debug("request: " + str(method) + " " + str(url))
    methods = _Methods

    if method == methods.TRACE or method == methods.CONNECT:
        raise NotImplemented
    else:
        r = getattr(requests, method.name.lower())(
            url=url, data=data
        )
    logger.debug("response: " + str(r.status_code) + " " + str(r.reason))
    if r.status_code != 200 and supress is False:
        logger.warning(f"request {str(method)} {str(url)} returned: {r.status_code} {Socket.Codes[r.status_code]}")
    return r


class Socket:
    Codes = _Codes
    Methods = _Methods
    Send_Request = _Send_Request

    def __init__(self, host, port, client):
        self.client = client
        self.host = host
        self.port = port
