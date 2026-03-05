from typing import List

from src.core.exceptions import DataNotFound
from src.schemas.jobs import JobsSchema, JobsAddSchema, JobsOptionalSchema
from src.services.base import BService


class JobService(BService):

    async def create_job(self, data: JobsAddSchema) -> JobsSchema:
        return JobsSchema.model_validate(await self.db.jobs.create(data))

    async def get_job_by_filter(self, data: JobsOptionalSchema) -> List[JobsSchema]:
        kwargs_filters = data.model_dump(exclude_unset=True, exclude_none=True)
        result = await self.db.user.get_by_filter(**kwargs_filters)
        if not result:
            raise DataNotFound(kwargs_filters)
        return result

    async def delete_by_id(self, job_id: int) -> None:
        job = await self.db.jobs.get_by_filter(job_id=job_id)
        if not job:
            raise DataNotFound({'job_id': job_id})
        await self.db.jobs.delete(job)

    async def update_job(self, data: JobsOptionalSchema, job_id: int):
        job = await self.db.jobs.get_by_filter(job_id=job_id)
        if not job:
            raise DataNotFound({'job_id': job_id})
        return JobsSchema.model_validate(
            await self.db.jobs.update(data, job_id)
        )


