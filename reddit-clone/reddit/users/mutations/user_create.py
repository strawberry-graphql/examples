from typing import Union, cast

import strawberry
from strawberry.types import Info

from reddit.database import get_session
from reddit.users.types import UserType
from reddit.users.services import UserService

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


async def resolve_user_create(info: Info, input: UserCreateInput) -> UserCreateResult:
    async with get_session() as session:
        service = UserService(session=session)
        user = await service.create_user(**input)
    return UserCreateSuccess(user=cast(UserType, user))


user_create = strawberry.mutation(
    resolver=resolve_user_create,
    description="""
    Creates a new user.
    """,
)
