from src.models.jobs import Works
from src.repositories.base import BaseRepo
from src.schemas.jobs import JobsSchema


class JobsRepo(BaseRepo):
    """Репозиторий работ (jobs)"""
    model = Works
    schema = JobsSchema