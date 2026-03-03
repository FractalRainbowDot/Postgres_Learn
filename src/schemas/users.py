from pydantic import BaseModel, Field, ConfigDict


class UsersSchema(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=125, )

    model_config = ConfigDict(from_attributes=True)


class BaseUserSchema(UsersSchema):
    id: int