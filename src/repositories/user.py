from src.models.users import UserModel
from src.repositories.base import BaseRepo
from src.schemas.users import FinalUserSchema


class UserRepo(BaseRepo):
    """Репозиторий пользователей (user)"""
    model = UserModel
    schema = FinalUserSchema