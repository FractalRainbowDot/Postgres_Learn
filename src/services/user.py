from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import DataNotFound
from src.repositories.user import UserRepo
from src.schemas.users import UsersSchema, FinalUserSchema, UserAddSchema, UserFilterSchema, UpdateUserSchema
from src.services.base import BService


class UserService(BService):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.user_repo = UserRepo(self.session)

    async def create_user(self, data: UserAddSchema) -> FinalUserSchema:
        return FinalUserSchema.model_validate(await self.user_repo.create(data))

    async def get_user_by_filter(self, data: UserFilterSchema) -> List[FinalUserSchema]:
        kwargs_filters = data.model_dump(exclude_unset=True, exclude_none=True)
        result = await self.user_repo.get_by_filter(**kwargs_filters)
        if not result:
            raise DataNotFound(kwargs_filters)
        return result

    async def delete_user_by_id(self, user_id: int) -> None:
        user = await self.user_repo.get_by_filter(user_id=user_id)
        if not user:
            raise DataNotFound({'user_id': user_id})
        await self.user_repo.delete_by_id(user_id)

    async def update_user(self, data: UpdateUserSchema, user_id: int) -> FinalUserSchema:
        user = await self.user_repo.get_by_filter(user_id=user_id)
        if not user:
            raise DataNotFound({'user_id': user_id})
        return FinalUserSchema.model_validate(
            await self.user_repo.update(data, user_id)
        )
