from typing import Optional
from main.models import User


SESSION_KEY = "_auth_user_id"


def login(request, user: User):
    session = request.session
    session[SESSION_KEY] = user.id


def logout(request):
    session = request.session
    del session[SESSION_KEY]


def get_user(db, request) -> Optional[User]:
    session = request.session
    if SESSION_KEY not in session:
        return None

    user = db.query(User).filter_by(id=request.session[SESSION_KEY]).first()

    return user
