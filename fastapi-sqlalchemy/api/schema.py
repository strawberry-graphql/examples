from typing import List

import strawberry
from strawberry.extensions import Extension

from main.models import get_movies
from main.database import SessionLocal

from .definitions.movie import Movie


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["db"] = SessionLocal()

    def on_request_end(self):
        self.execution_context.context["db"].close()


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"

    @strawberry.field
    def top_rated_movies(self, info, limit: int = 250) -> List[Movie]:
        db = info.context["db"]
        movies = get_movies(db, limit=limit)
        return [Movie.from_instance(movie) for movie in movies]


schema = strawberry.Schema(Query, extensions=[SQLAlchemySession])
