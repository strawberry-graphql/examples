from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType

__all__ = ("email_change",)


@strawberry.input
class EmailChangeInput:
    email: str
    change_code: str


@strawberry.type
class EmailChangeSuccess:
    user: UserType


@strawberry.type
class EmailChangeError:
    error: str


EmailChangeResult = Union[EmailChangeSuccess, EmailChangeError]


async def resolve_email_change(
    info: Info, input: EmailChangeInput
) -> EmailChangeResult:
    pass


email_change = strawberry.mutation(
    resolver=resolve_email_change,
    description="""
    Changes the email for associated user.
    """,
)