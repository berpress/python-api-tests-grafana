from fixtures.api.user.models.create_user import CreateUserRequets


class TestCreateClient:
    def test_create_client(self, app):
        """
        1. Create user with valid data
        2. check status code
        """
        data = CreateUserRequets.random()
        res = app.user.create_user(data=data)
        assert res.status_code == 200

    def test_create_client_invalid_data(self, app):
        """
        1. Create user with invalid data id
        2. check status code
        """
        data = CreateUserRequets.random()
        data.id = 'Test'
        res = app.user.create_user(data=data)
        assert res.status_code == 500
