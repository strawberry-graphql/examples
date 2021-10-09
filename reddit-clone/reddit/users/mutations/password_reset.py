import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


@strawberry.type
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


PasswordResetResult = strawberry.union(
    name="PasswordResetResult", types=(PasswordResetSuccess, PasswordResetError)
)


@strawberry.mutation(description="Resets the password for the user account.")
async def password_reset(info: Info, input: PasswordResetInput) -> PasswordResetResult:
    pass
