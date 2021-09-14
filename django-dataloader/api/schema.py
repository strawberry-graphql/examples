from typing import List
import strawberry

from movies.models import Movie as MovieModel
from .definitions.movie import Movie
from .extensions import SyncToAsync, PyInstrumentExtension, VizTracerExtension


@strawberry.type
class Query:
    @strawberry.field
    def top_rated_movies(self, info, limit: int = 250) -> List[Movie]:
        movies = MovieModel.objects.all().order_by("-imdb_rating")[:limit]
        return [Movie.from_instance(movie) for movie in movies]


schema = strawberry.Schema(Query, extensions=[SyncToAsync])
