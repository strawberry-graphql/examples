from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


__all__ = ("user_block",)


@strawberry.input
class UserBlockInput:
    user_id: strawberry.ID


@strawberry.type
class UserBlockSuccess:
    user: UserType


@strawberry.type
class UserBlockError:
    error: str


UserBlockResult = Union[UserBlockSuccess, UserBlockError]


async def resolve_user_block(info: Info, input: UserBlockInput) -> UserBlockResult:
    pass


user_block = strawberry.mutation(
    name="user_block",
    resolver=resolve_user_block,
    description="""
    Blocks an user account.
    """,
)
