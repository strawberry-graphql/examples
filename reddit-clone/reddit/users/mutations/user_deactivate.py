from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType

__all__ = ("user_deactivate",)


@strawberry.input
class UserDeactivateInput:
    password: str


@strawberry.type
class UserDeactivateSuccess:
    user: UserType


@strawberry.type
class UserDeactivateError:
    error: str


UserDeactivateResult = Union[UserDeactivateSuccess, UserDeactivateError]


async def resolve_user_deactivate(
    info: Info, input: UserDeactivateInput
) -> UserDeactivateResult:
    pass


user_deactivate = strawberry.mutation(
    resolver=resolve_user_deactivate,
    description="""
    Deactivates the current user.
    """,
)
