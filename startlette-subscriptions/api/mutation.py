from strawberry.tools import create_type

from .mutations.create_job import create_job
from .mutations.update_job_status import update_job_status

Mutation = create_type(
    "Mutation",
    [
        create_job,
        update_job_status,
    ],
)
