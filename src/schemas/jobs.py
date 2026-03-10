from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator

from src.core.exceptions import CounterNahryukError


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


class Requirements(str, Enum):
    MASTURBATING = 'masturbating'
    PROGRAMMING = 'programming'
    HUGE_DICK = 'huge dick'
    PYTHON = 'python'
    SQL = 'sql'
    DOCKER = 'docker'
    ALEMBIC = 'alembic'


class JobsAddSchema(ValidationSchema):
    title: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=2, max_length=150)
    salary: float = Field(gt=0)
    office_address: str = Field(min_length=2, max_length=50)
    requirements: List[Requirements] = Field(
        default_factory=list,
        json_schema_extra={"example": [r.value for r in Requirements]}
    )
    email: EmailStr = Field(min_length=5, max_length=50)
    cell_count: int = Field(None, ge=0)


class JobsSchema(JobsAddSchema):
    id: int
    is_active: bool = Field(default=True)

class JobsOptionalSchemaNoId(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=50)
    description: Optional[str] = Field(None, min_length=2, max_length=150)
    salary: Optional[float] = Field(None, gt=0)
    office_address: Optional[str] = Field(None, min_length=2, max_length=50)
    requirements: Optional[List[Requirements]] = None
    email: Optional[EmailStr] = Field(None, min_length=5, max_length=50)
    is_active: Optional[bool] = Field(None)
    id: Optional[int] = Field(None, gt=0)
    cell_count: Optional[int] = Field(None, ge=0)

class JobsOptionalSchema(BaseModel):
    id: Optional[int] = Field(None, gt=0)
