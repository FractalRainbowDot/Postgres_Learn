from typing import List

from src.core.exceptions import DataNotFound
from src.schemas.pagination import PaginationParams
from src.schemas.users import FinalUserSchema, UserAddSchema, UserFilterSchema, UpdateUserSchema
from src.services.base import BService


class UserService(BService):

    async def create_user(self, data: UserAddSchema) -> FinalUserSchema:
        return FinalUserSchema.model_validate(await self.db.user.create(data))

    async def get_user_by_filter(self, data: UserFilterSchema, limits: PaginationParams) -> List[FinalUserSchema]:
        kwargs_filters = data.model_dump(exclude_unset=True, exclude_none=True)
        result = await self.db.user.get_by_filter(limits, **kwargs_filters)
        if not result:
            raise DataNotFound(kwargs_filters)
        return result

    async def delete_user_by_id(self, user_id: int) -> None:
        user = await self.db.user.get_by_filter(user_id=user_id)
        if not user:
            raise DataNotFound({'user_id': user_id})
        await self.db.user.delete_by_id(user_id)

    async def update_user(self, data: UpdateUserSchema, user_id: int) -> FinalUserSchema:
        user = await self.db.user.get_by_filter(user_id=user_id)
        if not user:
            raise DataNotFound({'user_id': user_id})
        return FinalUserSchema.model_validate(
            await self.db.user.update(data, user_id)
        )
