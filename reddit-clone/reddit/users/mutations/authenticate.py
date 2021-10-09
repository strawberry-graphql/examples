import strawberry
from strawberry.types import Info

from reddit.users.types import UserType


@strawberry.type
class AuthenticateInput:
    username: str
    password: str


@strawberry.type
class AuthenticateSuccess:
    user: UserType


@strawberry.type
class AuthenticateError:
    error: str


AuthenticateResult = strawberry.union(
    name="AuthenticateResult", types=(AuthenticateSuccess, AuthenticateError)
)


@strawberry.mutation(description="Logs the current user in.")
async def authenticate(info: Info, input: AuthenticateInput) -> AuthenticateResult:
    pass
