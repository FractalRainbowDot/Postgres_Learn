from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.api.v1.endpoints.user import router as user_router
from src.api.v1.endpoints.jobs import router as jobs_router
from src.core.exceptions import ApplicationException

app = FastAPI(
    title="test",
)


@app.exception_handler(ApplicationException)
async def application_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


app.include_router(user_router)
app.include_router(jobs_router)
