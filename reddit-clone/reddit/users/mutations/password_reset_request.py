from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


@strawberry.type
class PasswordResetRequestInput:
    email: str


@strawberry.type
class PasswordResetRequestSuccess:
    user: UserType


@strawberry.type
class PasswordResetRequestError:
    error: str


PasswordResetRequestResult = Union[
    PasswordResetRequestSuccess, PasswordResetRequestError
]


@strawberry.mutation(description="Sends a password reset code to the given email.")
async def password_reset_request(
    info: Info, input: PasswordResetRequestInput
) -> PasswordResetRequestResult:
    pass
