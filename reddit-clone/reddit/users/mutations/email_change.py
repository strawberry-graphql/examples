from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


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


@strawberry.mutation(description="Changes the email for associated user.")
async def email_change(info: Info, input: EmailChangeInput) -> EmailChangeResult:
    pass
