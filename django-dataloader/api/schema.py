from typing import List
import strawberry

from movies.models import Movie as MovieModel
from .definitions.movie import Movie
from .definitions.director import load_directors
from .extensions import SyncToAsync, AddDataLoader


@strawberry.type
class Query:
    @strawberry.field
    def top_rated_movies(self, info, limit: int = 250) -> List[Movie]:
        movies = MovieModel.objects.all().order_by("-imdb_rating")[:limit]
        return [Movie.from_instance(movie) for movie in movies]


schema = strawberry.Schema(
    Query,
    extensions=[
        SyncToAsync,
        AddDataLoader("director_loader", load_fn=load_directors),  # type: ignore
    ],
)
