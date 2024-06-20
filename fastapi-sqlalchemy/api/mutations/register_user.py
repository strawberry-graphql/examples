import re
import strawberry

from main.auth import login
from main.models import User as UserModel, get_user_by_email

from ..definitions.user import User


@strawberry.input
class RegisterUserInput:
    email: str
    password: str


@strawberry.type
class RegisterUserSuccess:
    user: User


@strawberry.type
class RegisterUserError:
    error_message: str


RegisterUserResponse = strawberry.union(
    "RegisterUserResponse", types=(RegisterUserSuccess, RegisterUserError)
)


@strawberry.mutation
def register_user(info, data: RegisterUserInput) -> RegisterUserResponse:
    email = data.email
    password = data.password

    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        return RegisterUserError(error_message="Invalid email")

    if len(password) < 4:
        return RegisterUserError(error_message="Password too short")

    db = info.context["db"]

    existing_user = get_user_by_email(db, email)
    if existing_user:
        return RegisterUserError(error_message="User already exists")

    user = UserModel(
        email=email,
    )
    user.set_password(password)
    db.add(user)
    db.commit()

    # Login user
    login(info.context["request"], user)

    return RegisterUserSuccess(
        user=User.from_instance(user),
    )
