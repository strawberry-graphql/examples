from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


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
    pass
