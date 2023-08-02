from common.deco.request_logger import log
from fixtures.models.client import CustomResponse
from fixtures.models.response_model import Response as CustomResponse
from fixtures.structure import structure
from fixtures.api.user.models.create_user import CreateUserRequets


class Users:
    def __init__(self, app):
        self.app = app
        
    _POST_CREATE_USER = 'v2/user'

    @log('This can only be done by the logged in user.')
    def create_user(self, data: CreateUserRequets):
        """
        https://petstore.swagger.io/user/createUser # noqa
        """
        response = self.app.http_client.request(
            method="POST",
            url=f"{self.app.url}/{self._POST_CREATE_USER}",
            json=data.model_dump(),
        )
        return structure(response=response, type_response=CustomResponse)
