from abc import ABC, abstractmethod
from typing import List
from domain.entities import User

class AbstractUserRepository(ABC):
    """
    Абстрактный репозиторий (контракт), определяющий методы
    для работы с данными пользователей.
    """
    
    @abstractmethod
    async def add(self, user: User) -> User:
        """Добавляет нового пользователя."""
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[User]:
        """Возвращает всех пользователей."""
        raise NotImplementedError
