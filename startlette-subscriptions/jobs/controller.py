import uuid


from . import JOBS, JobModel
from .subscription_hub import hub


def get_job(id: str) -> JobModel:
    if id not in JOBS:
        raise Exception(f"Can't find job: {id}")

    return JOBS[id]


def create_job() -> JobModel:
    id = str(uuid.uuid4())
    model = JobModel(id=id, status="pending")
    JOBS[id] = model
    return model


def update_status(id: str, status: str) -> JobModel:
    job = get_job(id)
    job.status = status

    hub.update_job(id, job)

    return job
