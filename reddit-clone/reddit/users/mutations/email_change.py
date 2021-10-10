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
    name="email_change",
    resolver=resolve_email_change,
    description="""
    Changes the email for the user account
    associated with the given email.
    """,
)
