import strawberry


from jobs import controller
from ..defintions.job import Job, JobStatus


@strawberry.mutation
def update_job_status(id: str, status: JobStatus) -> Job:
    model = controller.update_status(id, status.value)
    return Job.from_instance(model)
