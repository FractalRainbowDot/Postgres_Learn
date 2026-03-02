from pydantic import BaseModel, Field
from typing import Optional

class UserCreateRequest(BaseModel):
    """
    DTO для создания пользователя.
    Клиент отправляет эти данные в теле запроса.
    """
    name: str = Field(..., min_length=1, description="Имя пользователя")
    surname: str = Field(..., min_length=1, description="Фамилия пользователя")
    age: int = Field(..., gt=0, description="Возраст пользователя")

class UserResponse(BaseModel):
    """
    DTO для ответа API.
    Возвращаем клиенту полную информацию о пользователе.
    """
    id: int
    name: str
    surname: str
    age: int

    class Config:
        from_attributes = True
