from src.repositories.user import UserRepo
from src.schemas.users import UsersSchema, BaseUserSchema
from src.services.base import BService


class UserService(BService):
    async def create_user(self, data: UsersSchema) -> BaseUserSchema:
          user_repo = UserRepo(self.session)
          return BaseUserSchema.model_validate(await user_repo.create(data))