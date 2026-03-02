from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5433/mydatabase"

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
