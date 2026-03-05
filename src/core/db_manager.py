from src.repositories.jobs import JobsRepo
from src.repositories.user import UserRepo


class DBManager:
    """Фабрика репозиториев"""
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.user = UserRepo(self.session)
        self.jobs = JobsRepo(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit