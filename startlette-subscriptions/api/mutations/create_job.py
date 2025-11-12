import strawberry


from jobs import controller
from ..defintions.job import Job


@strawberry.mutation
def create_job() -> Job:
    model = controller.create_job()
    return Job.from_instance(model)
