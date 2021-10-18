from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType

__all__ = ("email_change",)


@strawberry.input
class EmailChangeInput:
    email: str
    change_code: str
    password: str


@strawberry.type
class EmailChangeSuccess:
    user: UserType


@strawberry.type
class EmailChangeError:
    error: str


EmailChangeResult = Union[EmailChangeSuccess, EmailChangeError]


@strawberry.mutation(
    description="""
    Changes the email for the user account
    associated with the given email.
    """
)
async def email_change(info: Info, input: EmailChangeInput) -> EmailChangeResult:
    pass
