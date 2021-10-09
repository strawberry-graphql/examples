import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


@strawberry.type
class EmailChangeInput:
    email: str
    change_code: str


@strawberry.type
class EmailChangeSuccess:
    user: UserType


@strawberry.type
class EmailChangeError:
    error: str


EmailChangeResult = strawberry.union(
    name="EmailChangeResult", types=(EmailChangeSuccess, EmailChangeError)
)


@strawberry.mutation(description="Changes the email for associated user.")
async def email_change(info: Info, input: EmailChangeInput) -> EmailChangeResult:
    pass
