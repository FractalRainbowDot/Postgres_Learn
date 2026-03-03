from typing import Any, Type

from pydantic import BaseModel
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users import UserModel
from src.schemas.users import BaseUserSchema


class BaseRepo:
    model: Any = None
    schema: Type[BaseModel] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: BaseModel) -> BaseModel:
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self.schema.model_validate(result.scalars().first())

    async def get_by_filter(self, **kwargs_filters) -> BaseModel:
        query = select(self.model).filter_by(**kwargs_filters)
        result = await self.session.execute(query)
        return self.schema.model_validate(result.scalars().first())

    async def delete_by_id(self, id: int) -> None:
        stmt = delete(self.model).where(id == self.model.id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def update(self, data: BaseModel, id: int) -> BaseModel:
        stmt = update(self.model).where(id == self.model.id).values(**data.model_dump())
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self.schema.model_validate(result.scalars().first())

