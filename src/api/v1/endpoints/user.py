from typing import List
from fastapi import APIRouter, Depends

from src.core.engine import DBDep, PaginationDep
from src.schemas.pagination import PaginationParams
from src.schemas.users import UserAddSchema, FinalUserSchema, UserFilterSchema, UpdateUserSchema
from src.services.user import UserService

router = APIRouter(prefix="/user", tags=["User_routers"])


@router.post("/", response_model=FinalUserSchema)
async def user_add(
        db: DBDep,
        data: UserAddSchema
) -> FinalUserSchema:
    return await UserService(db).create_user(data)


@router.get("/", response_model=List[FinalUserSchema])
async def user_get_by_filters(
        db: DBDep,
        data: UserFilterSchema = Depends(),
        limits: PaginationParams = Depends()
) -> List[FinalUserSchema]:
    return await UserService(db).get_user_by_filter(data, limits)


@router.delete("/{user_id}")
async def delete_user(
        db: DBDep,
        user_id: int,
):
    await UserService(db).delete_user_by_id(user_id)
    return {'message': 'ok'}


@router.patch("/{user_id}", response_model=FinalUserSchema)
async def update_user(
        db: DBDep,
        user_id: int,
        data: UpdateUserSchema,
) -> FinalUserSchema:
    return await UserService(db).update_user(data, user_id)
