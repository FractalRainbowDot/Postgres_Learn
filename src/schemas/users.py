from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator

from src.core.exceptions import CounterNahryukError


class Gender(str, Enum):
    """Enum схема"""
    MALE = 'male'
    FEMALE = 'female'


class ValidationSchema(BaseModel):
    """Схема валидации данных"""

    @field_validator('email', check_fields=False)
    def check_email(cls, email):
        if email is None:
            return email
        forbidden_emails = {"@i.ua", "@ua.fm", "@email.ua", "@ukr.net"}
        if any(domain in email for domain in forbidden_emails):
            raise CounterNahryukError()
        return email

    model_config = ConfigDict(from_attributes=True)


class UserAddSchema(ValidationSchema):
    """Схема добавления пользователей(users)"""
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=125, )
    gender: Gender
    email: EmailStr = Field(min_length=2, max_length=50)
    password: str = Field(min_length=1, max_length=50)


class FinalUserSchema(UserAddSchema):
    """Общая схема пользователей (users)"""
    is_active: bool
    id: int


class UserFilterSchema(ValidationSchema):
    """Схема фильтров пользователей без пароля (users)"""
    name: Optional[str] = Field(None, min_length=2, max_length=20)
    surname: Optional[str] = Field(None, min_length=2, max_length=50)
    age: Optional[int] = Field(None, gt=0, lt=125)
    gender: Optional[Gender] = None
    email: Optional[EmailStr] = Field(None, min_length=2, max_length=50)
    is_active: Optional[bool] = Field(None)


class UpdateUserSchema(UserFilterSchema):
    """Схема фильтров с паролем"""
    password: Optional[str] = Field(None, min_length=1, max_length=50)


if __name__ == "__main__":
    print('4len')
