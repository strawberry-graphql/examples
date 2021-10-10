from typing import Union

import strawberry
from strawberry.file_uploads import Upload
from strawberry.types import Info

from reddit.users.types import UserType

__all__ = ("user_update",)


@strawberry.input
class UserUpdateInput:
    username: str
    avatar: Upload


@strawberry.type
class UserUpdateSuccess:
    user: UserType


@strawberry.type
class UserUpdateError:
    error: str


UserUpdateResult = Union[UserUpdateSuccess, UserUpdateError]


async def resolve_user_update(info: Info, input: UserUpdateInput) -> UserUpdateResult:
    pass


user_update = strawberry.mutation(
    name="user_update",
    resolver=resolve_user_update,
    description="""
    Updates the current user.
    """,
)
