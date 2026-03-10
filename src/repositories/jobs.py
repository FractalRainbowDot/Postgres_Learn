from src.models.jobs import JobsModel
from src.repositories.base import BaseRepo
from src.schemas.jobs import JobsSchema


class JobsRepo(BaseRepo):
    """Репозиторий работ (jobs)"""
    model = JobsModel
    schema = JobsSchema