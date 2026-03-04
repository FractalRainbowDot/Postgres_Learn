from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config import settings


engine = create_async_engine(settings.get_db_url())
engine_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_engine_session():
    async with engine_session() as session:
        yield session

sessionDep = Depends(get_engine_session)