from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.setup import AsyncSessionMaker
from infrastructure.database.repository import SQLAlchemyUserRepository
from application.use_cases import AddUserUseCase, GetAllUsersUseCase
from application.repositories import AbstractUserRepository

# 1. Получение сессии БД
async def get_db_session():
    async with AsyncSessionMaker() as session:
        yield session

# 2. Адаптер для репозитория
class SessionRepositoryAdapter(SQLAlchemyUserRepository):
    """
    Адаптер, позволяющий использовать уже открытую сессию FastAPI
    вместо создания новой через session_maker.
    """
    def __init__(self, session: AsyncSession):
        self.session = session
        # Переопределяем async_session_maker, чтобы он возвращал контекстный менеджер с текущей сессией
        self.async_session_maker = lambda: self._fake_session_manager()

    def _fake_session_manager(self):
        class FakeContextManager:
            def __init__(self, session):
                self.session = session
            async def __aenter__(self):
                return self.session
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass # Не закрываем сессию здесь, это сделает FastAPI
        return FakeContextManager(self.session)

# 3. Получение репозитория (зависит от сессии)
def get_repository(session: AsyncSession = Depends(get_db_session)) -> AbstractUserRepository:
    return SessionRepositoryAdapter(session)

# 4. Получение Use Case'ов (зависят от репозитория)
def get_add_user_use_case(repo: AbstractUserRepository = Depends(get_repository)) -> AddUserUseCase:
    return AddUserUseCase(repo)

def get_get_all_users_use_case(repo: AbstractUserRepository = Depends(get_repository)) -> GetAllUsersUseCase:
    return GetAllUsersUseCase(repo)
