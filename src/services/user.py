from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.user import UserRepo
from src.schemas.users import UsersSchema, BaseUserSchema, UserAddSchema
from src.services.base import BService


class UserService(BService):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.user_repo = UserRepo(self.session)

    async def create_user(self, data: UserAddSchema) -> BaseUserSchema:
        return BaseUserSchema.model_validate(await self.user_repo.create(data))

    async def get_user_by_filter(self, **kwargs_filters) -> BaseUserSchema:
        return BaseUserSchema.model_validate(await self.user_repo.get_by_filter(**kwargs_filters))

    async def delete_user_by_id(self, user_id: int) -> None:
        await self.user_repo.delete_by_id(user_id)

    async def update_user(self, data: UsersSchema, user_id: int) -> BaseUserSchema:
        return BaseUserSchema.model_validate(
            await self.user_repo.update(data.model_dump(exclude_unset=True), user_id)
        )


