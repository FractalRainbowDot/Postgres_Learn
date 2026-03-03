from enum import Enum

from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator

from src.core.exceptions import CounterNahryukError


class Gender(Enum):
    MALE='male'
    FEMALE='female'

class UsersSchema(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=125, )
    gender: Gender
    email: EmailStr = Field(min_length=2, max_length=50)
    password: str = Field(min_length=4, max_length=8)
    is_active: bool

    @field_validator('email')
    def check_email(cls, email):
        forbidden_emails = {"@i.ua", "@ua.fm", "@email.ua", "@ukr.net"}
        if any(forbidden_emails) in email:
            raise CounterNahryukError()
        return email

    model_config = ConfigDict(from_attributes=True)


class BaseUserSchema(UsersSchema):
    id: int