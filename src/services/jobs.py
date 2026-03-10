from typing import List

from src.core.exceptions import DataNotFound
from src.schemas.jobs import JobsSchema, JobsAddSchema, JobsOptionalSchema, JobsOptionalSchemaNoId
from src.schemas.pagination import PaginationParams
from src.services.base import BService


class JobService(BService):

    async def create_job(self, data: JobsAddSchema) -> JobsSchema:
        return JobsSchema.model_validate(await self.db.jobs.create(data))

    async def get_job_by_filter(self, data: JobsOptionalSchema, limits: PaginationParams = None) -> List[JobsSchema]:
        kwargs_filters = data.model_dump(exclude_unset=True, exclude_none=True)
        result = await self.db.jobs.get_by_filter(limits, **kwargs_filters)
        if not result:
            raise DataNotFound(kwargs_filters)
        return result

    async def delete_by_id(self, id: int) -> None:
        job = await self.db.jobs.get_by_filter(id=id)
        if not job:
            raise DataNotFound({'id': id})
        await self.db.jobs.delete_by_id(id)

    async def update_job(self, data: JobsOptionalSchemaNoId, id: int):
        job = await self.db.jobs.get_by_filter(id=id)
        if not job:
            raise DataNotFound({'id': id})
        return JobsSchema.model_validate(
            await self.db.jobs.update(data, id)
        )
