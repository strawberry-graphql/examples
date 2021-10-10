from typing import Union, cast

import strawberry
from strawberry.types import Info

from reddit.database import get_session
from reddit.users.types import UserType
from reddit.users.services import UserService


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
    async with get_session() as session:
        service = UserService(session=session)
        user = await service.authenticate(**input)
    if user is None:
        return AuthenticateError(error="Invalid credentials provided.")
    return AuthenticateSuccess(user=cast(UserType, user))


authenticate = strawberry.mutation(
    resolver=resolve_authenticate,
    description="""
    Logs the current user in.
    """,
)
