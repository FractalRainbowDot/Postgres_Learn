from sqlalchemy.ext.asyncio import AsyncSession


class BService:
    def __init__(self, session: AsyncSession):
        self.session = session