from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


__all__ = ("email_change_request",)


@strawberry.input
class EmailChangeRequestInput:
    email: str
    password: str


@strawberry.type
class EmailChangeRequestSuccess:
    user: UserType


@strawberry.type
class EmailChangeRequestError:
    error: str


EmailChangeRequestResult = Union[EmailChangeRequestSuccess, EmailChangeRequestError]


@strawberry.mutation(
    description="""
    Sends an email change code to
    the given email address.
    """
)
async def email_change_request(
    info: Info, input: EmailChangeRequestInput
) -> EmailChangeRequestResult:
    pass
