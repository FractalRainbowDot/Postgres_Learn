from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.engine import sessionDep
from src.schemas.users import UserAddSchema, FinalUserSchema, UserFilterSchema, UsersSchema
from src.services.user import UserService

router = APIRouter(prefix="/user", tags=["User_routers"])


@router.post("/", response_model=FinalUserSchema)
async def user_add(data: UserAddSchema,
                   session: AsyncSession = sessionDep) -> FinalUserSchema:
    return await UserService(session).create_user(data)

@router.get("/", response_model=List[FinalUserSchema])
async def user_get_by_filters(data: UserFilterSchema = Depends(),
                   session: AsyncSession = sessionDep) -> List[FinalUserSchema]:
    return await UserService(session).get_user_by_filter(data)

@router.delete("/")
async def delete_user(user_id: int,
                      session: AsyncSession = sessionDep):
    await UserService(session).delete_user_by_id(user_id)
    return {'message': 'ok'}

@router.patch("/")
async def update_user(data: UsersSchema,
                      user_id: int,
                      session: AsyncSession = sessionDep) -> FinalUserSchema:
    return await UserService(session).update_user(data, user_id)
    