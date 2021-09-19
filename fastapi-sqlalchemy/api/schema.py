from typing import List

import strawberry
from strawberry.extensions import Extension

from main.models import get_movies, get_people
from main.database import SessionLocal

from .definitions.movie import Movie
from .definitions.people import Person


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
    def all_people(self, info) -> List[Person]:
        db = info.context["db"]
        people = get_people(db)
        return [Person.from_instance(person) for person in people]

    @strawberry.field
    def all_people_queryset(self, info) -> List[Person]:
        db = info.context["db"]
        return get_people(db)


schema = strawberry.Schema(Query, extensions=[SQLAlchemySession])
