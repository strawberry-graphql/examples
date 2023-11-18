from typing import List, Optional

import strawberry
from strawberry.extensions import Extension

from main.models import get_movies
from main.database import SessionLocal

from .mutation import Mutation
from .definitions.movie import Movie
from .definitions.user import User


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["db"] = SessionLocal()

    def on_request_end(self):
        self.execution_context.context["db"].close()


@strawberry.type
class Query:
    @strawberry.field
    def top_rated_movies(self, info, limit: int = 250) -> List[Movie]:
        db = info.context["db"]
        movies = get_movies(db, limit=limit)
        return [Movie.from_instance(movie) for movie in movies]

    @strawberry.field
    def current_user(self, info) -> Optional[User]:
        request = info.context["request"]

        if request.user.is_authenticated:
            return User.from_instance(request.user)

        return None


schema = strawberry.Schema(Query, mutation=Mutation, extensions=[SQLAlchemySession])
