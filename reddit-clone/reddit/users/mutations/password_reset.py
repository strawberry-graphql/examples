from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType

__all__ = ("password_reset",)


@strawberry.input
class PasswordResetInput:
    password: str
    reset_code: str
    email: str


@strawberry.type
class PasswordResetSuccess:
    user: UserType


@strawberry.type
class PasswordResetError:
    error: str


PasswordResetResult = Union[PasswordResetSuccess, PasswordResetError]


async def resolve_password_reset(
    info: Info, input: PasswordResetInput
) -> PasswordResetResult:
    pass


password_reset = strawberry.mutation(
    resolver=resolve_password_reset,
    description="""
    Resets the password for the user account
    associated with the given email.
    """,
)
