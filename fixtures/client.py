from fixtures.api.user.api import Users
from fixtures.requests import HTTPClient


class ClientApi:
    def __init__(self, url: str):
        self.url = url
        self.http_client = HTTPClient
        self.user = Users(self)
