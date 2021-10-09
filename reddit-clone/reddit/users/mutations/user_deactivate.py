from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


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


@strawberry.mutation(description="Deactivates the current user.")
async def user_deactivate(
    info: Info, input: UserDeactivateInput
) -> UserDeactivateResult:
    pass
