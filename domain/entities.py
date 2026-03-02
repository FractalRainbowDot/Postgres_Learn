from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    """
    Доменная сущность 'Пользователь'.
    Это ядро бизнес-логики, не зависит ни от каких фреймворков.
    """
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    surname: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)

    class Config:
        from_attributes = True # Заменено с orm_mode для Pydantic v2
