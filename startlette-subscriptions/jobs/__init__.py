from typing import Dict
from dataclasses import dataclass


@dataclass
class JobModel:
    id: str
    status: str


# Map of created jobs
JOBS: Dict[str, JobModel] = {}
