from typing import List
from sqlalchemy import select, func
from domain.entities import User
from application.repositories import AbstractUserRepository
from .models import UserDB

class SQLAlchemyUserRepository(AbstractUserRepository):
    """
    Конкретная реализация репозитория с использованием SQLAlchemy.
    Этот класс знает, как работать с сессиями и ORM-моделями.
    """
    def __init__(self, async_session_maker):
        self.async_session_maker = async_session_maker

    async def add(self, user: User) -> User:
        async with self.async_session_maker() as session:
            query = select(func.count(UserDB.id)).where(UserDB.name == user.name, UserDB.surname == user.surname)
            result = await session.execute(query)
            if result.scalar_one() > 0:
                print(f"Репозиторий: Пользователь {user.name} {user.surname} уже существует.")
                return user

            db_user = UserDB(**user.model_dump(exclude_unset=True))
            session.add(db_user)
            await session.commit()
            await session.refresh(db_user)
            print(f"Репозиторий: Пользователь {db_user.name} {db_user.surname} успешно добавлен.")
            return User.from_orm(db_user)

    async def get_all(self) -> List[User]:
        async with self.async_session_maker() as session:
            query = select(UserDB).order_by(UserDB.id)
            result = await session.execute(query)
            db_users = result.scalars().all()
            return [User.from_orm(user) for user in db_users]
