from typing import Any, Type, List, Optional

from pydantic import BaseModel
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.pagination import PaginationParams


class BaseRepo:
    """Базовый репозиторий"""
    model: Any = None
    schema: Type[BaseModel] = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: BaseModel) -> BaseModel:
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self.schema.model_validate(result.scalars().first())

    async def get_by_filter(self, pagination: Optional[PaginationParams] = None, **kwargs_filters) -> List[BaseModel]:
        if pagination is None:
            pagination = PaginationParams(limit=10, offset=0)
        query = select(self.model).limit(pagination.limit).offset(pagination.offset).filter_by(**kwargs_filters)
        result = await self.session.execute(query)
        return [self.schema.model_validate(item) for item in result.scalars().all()]

    async def delete_by_id(self, id: int) -> None:
        stmt = delete(self.model).where(id == self.model.id)
        await self.session.execute(stmt)
        await self.session.commit()

    async def update(self, data: BaseModel, id: int) -> Optional[BaseModel]:
        update_data = data.model_dump(exclude_unset=True)
        stmt = (
            update(self.model)
            .where(id == self.model.id)
            .values(**update_data)
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        db_obj = result.scalars().first()
        if db_obj:
            return self.schema.model_validate(db_obj)
        return None
