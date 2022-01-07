import requests
from enum import Enum

class http:
    resFile = "Helper/response_codes.txt"

    class methods(Enum):
        GET = 1
        HEAD = 2
        POST = 3
        PUT = 4
        DELETE = 5
        CONNECT = 6
        OPTIONS = 7
        TRACE = 8

    def sendRequest(
            method=methods.GET,
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
            cert=None
    ):
        methods = http.methods

        if method == methods.TRACE or method == methods.CONNECT:
            raise NotImplemented
        else:
            r = getattr(requests, method.name.lower())(
                url=url, data=data
            )
        if (r.status_code != 200):
            print(f"{r.status_code} {http.findCode(r.status_code)}")
        return r


    def findCode(code):
        list = []
        f = open(http.resFile)
        list = f.readlines()

        for line in list:
            if line.startswith(f"{code}"):
                ans = line.split("=")[1]

        return ans