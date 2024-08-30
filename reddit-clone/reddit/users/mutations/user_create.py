from typing import Union, cast
from marshmallow.exceptions import ValidationError

import strawberry
from strawberry.types import Info

from reddit.database import get_session
from reddit.users.types import UserType
from reddit.users.serializers import user_schema
from reddit.users.services import user_by_email, user_by_username, create_user

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
        data = user_schema.load(
            {
                "username": input.username,
                "password": input.password,
                "email": input.email,
            }
        )
    except ValidationError as err:
        # TODO: handle validation errors here.
        print(err)
        return UserCreateError(error=str(err))

    async with get_session() as session:
        if await user_by_email(session=session, email=data.get("email")):
            return UserCreateError(error="Email already exists.")
        if await user_by_username(session=session, username=data.get("username")):
            return UserCreateError(error="Username already exists.")

        user = await create_user(
            session=session,
            email=data.get("email"),
            username=data.get("username"),
            password=data.get("password"),
        )
    return UserCreateSuccess(user=cast(UserType, user))
