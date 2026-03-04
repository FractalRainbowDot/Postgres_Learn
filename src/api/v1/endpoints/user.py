from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.engine import get_engine_session
from src.schemas.users import UserAddSchema, BaseUserSchema
from src.services.user import UserService

router = APIRouter(prefix="/user", tags=["User_routers"])


@router.post("/", response_model=BaseUserSchema)
async def user_add(data: UserAddSchema,
                   session: AsyncSession = Depends(get_engine_session)):
    return await UserService(session).create_user(data)
