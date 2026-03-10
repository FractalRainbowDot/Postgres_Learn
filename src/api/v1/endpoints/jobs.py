from fastapi import APIRouter

from src.core.engine import DBDep
from src.schemas.jobs import JobsAddSchema, JobsSchema
from src.services.jobs import JobService

router = APIRouter(prefix='/jobs', tags=['Jobs_routers'])

@router.post("/")
async def job_add(
        db: DBDep,
        data: JobsAddSchema
) -> JobsSchema:
    return await JobService(db).create_job(data)