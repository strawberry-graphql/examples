import re
import strawberry

from main.auth import login
from main.models import User as UserModel

from ..definitions.user import User


@strawberry.type
class LoginUserSuccess:
    user: User


@strawberry.type
class LoginUserError:
    error_message: str


LoginUserResponse = strawberry.union(
    "LoginUserResponse", types=(LoginUserSuccess, LoginUserError)
)


@strawberry.mutation
def login_user(info, email: str, password: str) -> LoginUserResponse:
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        return LoginUserError(error_message="Invalid email")

    db = info.context["db"]

    user = db.query(UserModel).filter_by(email=email).first()
    if not user:
        return LoginUserError(error_message="User not found")

    if not user.check_password(password):
        return LoginUserError(error_message="Invalid password")

    # Login user
    login(info.context["request"], user)

    return LoginUserSuccess(
        user=User.from_instance(user),
    )
