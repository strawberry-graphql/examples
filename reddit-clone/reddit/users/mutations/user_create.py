from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType

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
    pass


user_create = strawberry.mutation(
    resolver=resolve_user_create,
    description="""
    Creates a new user.
    """,
)
