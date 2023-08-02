from faker import Faker
from pydantic import BaseModel

fake = Faker()


class CreateUserRequets(BaseModel):
    id: int | None
    username: str | None
    firstName: str | None
    lastName: str | None
    email: str | None
    password: str | None
    phone: str | None
    userStatus: int | None

    @staticmethod
    def random():
        id_ = 0
        username = fake.name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        user_status = 0
        return CreateUserRequets(
            id=id_,
            firstName=first_name,
            username=username,
            lastName=last_name,
            email=email,
            password=password,
            phone=phone,
            userStatus=user_status
        )
