from src.models.users import UserModel
from src.repositories.base import BaseRepo
from src.schemas.users import FinalUserSchema


class UserRepo(BaseRepo):
    model = UserModel
    schema = FinalUserSchema