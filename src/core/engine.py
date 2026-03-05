from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.core.config import settings
from src.core.db_manager import DBManager
from src.schemas.pagination import PaginationParams

engine = create_async_engine(
    settings.get_db_url(),
    echo=False,
    pool_pre_ping=True
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


async def get_db():
    """Получить сессию DB"""
    async with DBManager(session_factory=async_session_factory) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]

PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]
