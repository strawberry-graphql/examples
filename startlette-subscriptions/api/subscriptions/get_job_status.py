from typing import AsyncGenerator

import strawberry


from jobs import controller
from jobs.subscription_hub import hub

from ..defintions.job import Job


@strawberry.subscription
async def get_job_status(id: str) -> AsyncGenerator[Job, None]:
    # Look up job id
    job = controller.get_job(id)

    yield Job.from_instance(job)

    try:
        queue = hub.subscribe_to_job(id)
        while (val := await queue.get()) is not None:
            yield Job.from_instance(val)
    finally:
        hub.unsubscribe(id, queue)
