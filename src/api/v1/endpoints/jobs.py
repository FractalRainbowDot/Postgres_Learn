from typing import Optional, List

from fastapi import APIRouter, Depends

from src.core.engine import DBDep
from src.schemas.jobs import JobsAddSchema, JobsSchema, JobsOptionalSchema, JobsOptionalSchemaNoId
from src.schemas.pagination import PaginationParams
from src.services.jobs import JobService

router = APIRouter(prefix='/jobs', tags=['Jobs_routers'])

@router.post("/")
async def job_add(
        db: DBDep,
        data: JobsAddSchema
) -> JobsSchema:
    return await JobService(db).create_job(data)

@router.get("/")
async def job_get_all(
        db: DBDep,
        limits: PaginationParams = Depends()
) -> List[JobsSchema]:
    return await JobService(db).get_job_by_filter(data=JobsOptionalSchema(), limits=limits)

@router.post("/search")
async def job_search_by_filters(
        db: DBDep,
        data: JobsOptionalSchema = Depends(),
        limits: PaginationParams = Depends()
) -> List[JobsSchema]:
    return await JobService(db).get_job_by_filter(data=data, limits=limits)

@router.delete("/{job_id}")
async def delete_job(
        db: DBDep,
        job_id: int
):
    await JobService(db).delete_by_id(job_id)
    return {'message': 'ok'}

@router.patch("/{job_id}")
async def update_job(
        db: DBDep,
        job_id: int,
        data: JobsOptionalSchemaNoId = Depends()
) -> JobsSchema:
    return await JobService(db).update_job(data, job_id)