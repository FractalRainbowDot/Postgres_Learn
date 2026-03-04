from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator

from src.core.exceptions import CounterNahryukError


class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'


class ValidationSchema(BaseModel):
    @field_validator('email', check_fields=False)
    def check_email(cls, email):
        if email is None:
            return email
        forbidden_emails = {"@i.ua", "@ua.fm", "@email.ua", "@ukr.net"}
        if any(domain in email for domain in forbidden_emails):
            raise CounterNahryukError()
        return email


class UserGetSchema(BaseModel):
    user_id: int


class UserBaseSchema(ValidationSchema):
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=125, )
    gender: Gender
    email: EmailStr = Field(min_length=2, max_length=50)


class UserAddSchema(UserBaseSchema):
    password: str = Field(min_length=4, max_length=8)


class UsersSchema(UserAddSchema):
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class FinalUserSchema(UsersSchema):
    user_id: int


class UserFilterSchema(ValidationSchema):
    name: Optional[str] = Field(None, min_length=2, max_length=20)
    surname: Optional[str] = Field(None, min_length=2, max_length=50)
    age: Optional[int] = Field(None, gt=0, lt=125)
    gender: Optional[Gender] = None
    email: Optional[EmailStr] = Field(None, min_length=2, max_length=50)


class UpdateUserSchema(UserFilterSchema):
    password: Optional[str] = Field(None, min_length=4, max_length=8)
    is_active: Optional[bool] = Field(None)


if __name__ == "__main__":
    user = UpdateUserSchema(name='Oleg', age=20)
    print(repr(user))
