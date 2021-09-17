from enum import Enum
import strawberry

from jobs import JobModel


@strawberry.enum
class JobStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILURE = "FAILURE"


@strawberry.type
class Job:
    id: str
    status: JobStatus

    @classmethod
    def from_instance(cls, instance: JobModel):
        return cls(
            id=instance.id,
            status=JobStatus(instance.status),
        )
