from typing import List

import strawberry

from .definitions.movie import Movie


@strawberry.type
class Query:
    @strawberry.field
    # TODO: Add a resolver for this field
    def top_rated_movies(self, info, limit: int = 250) -> List[Movie]:
        return []


schema = strawberry.Schema(Query)
