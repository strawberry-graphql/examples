import strawberry

from jobs import controller

from .mutation import Mutation
from .subscription import Subscription
from .defintions.job import Job


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"

    @strawberry.field
    def get_job_by_id(self, id: str) -> Job:
        return Job.from_instance(controller.get_job(id))


schema = strawberry.Schema(Query, mutation=Mutation, subscription=Subscription)
