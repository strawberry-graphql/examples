from typing import Union
from marshmallow.exceptions import ValidationError

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType
from reddit.users.serializers import user_schema
from reddit.users.services import user_by_email, user_by_username

__all__ = ("user_create",)


@strawberry.input
class UserCreateInput:
    email: str
    username: str
    password: str


@strawberry.type
class UserCreateSuccess:
    user: UserType


@strawberry.type
class UserCreateError:
    error: str


UserCreateResult = Union[UserCreateSuccess, UserCreateError]


@strawberry.mutation(description="Creates a new user.")
async def user_create(info: Info, input: UserCreateInput) -> UserCreateResult:
    try:
        data = user_schema.load(input)
    except ValidationError as err:
        # TODO: handle validation errors here.
        print(err)

    if await user_by_email(email=data.get("email")):
        return UserCreateError(error="Email already exists.")
    if await user_by_username(username=data.get("username")):
        return UserCreateError(error="Username already exists.")
