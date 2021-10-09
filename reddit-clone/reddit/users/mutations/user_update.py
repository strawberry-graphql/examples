from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


@strawberry.type
class UserUpdateInput:
    email: str
    username: str
    password: str


@strawberry.type
class UserUpdateSuccess:
    user: UserType


@strawberry.type
class UserUpdateError:
    error: str


UserUpdateResult = Union[UserUpdateSuccess, UserUpdateError]


@strawberry.mutation(description="Updates the current user.")
async def user_update(info: Info, input: UserUpdateInput) -> UserUpdateResult:
    pass
