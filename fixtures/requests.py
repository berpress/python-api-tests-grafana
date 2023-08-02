

from requests import request


class HTTPClient:
    @staticmethod
    def request(method: str, url: str, **kwargs):
        return request(method=method, url=url, **kwargs)
