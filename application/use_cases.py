from typing import List
from domain.entities import User
from .repositories import AbstractUserRepository

class AddUserUseCase:
    """Сценарий использования для добавления пользователя."""
    def __init__(self, user_repo: AbstractUserRepository):
        self._user_repo = user_repo

    async def execute(self, user: User) -> User:
        # Здесь может быть сложная бизнес-логика: проверки, уведомления и т.д.
        print(f"Use Case: Попытка добавить пользователя {user.name} {user.surname}")
        return await self._user_repo.add(user)

class GetAllUsersUseCase:
    """Сценарий использования для получения всех пользователей."""
    def __init__(self, user_repo: AbstractUserRepository):
        self._user_repo = user_repo

    async def execute(self) -> List[User]:
        print("Use Case: Запрос на получение всех пользователей")
        return await self._user_repo.get_all()
