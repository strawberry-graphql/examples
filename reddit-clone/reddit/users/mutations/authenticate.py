from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


__all__ = ("authenticate",)


@strawberry.input
class AuthenticateInput:
    username: str
    password: str


@strawberry.type
class AuthenticateSuccess:
    user: UserType


@strawberry.type
class AuthenticateError:
    error: str


AuthenticateResult = Union[AuthenticateSuccess, AuthenticateError]


async def resolve_authenticate(
    info: Info, input: AuthenticateInput
) -> AuthenticateResult:
    pass


authenticate = strawberry.mutation(
    resolver=resolve_authenticate,
    description="""
    Logs the current user in.
    """,
)
