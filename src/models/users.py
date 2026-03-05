from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.schemas.users import Gender


class UserModel(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, )
    surname: Mapped[str] = mapped_column(String(50), nullable=False, )
    age: Mapped[int] = mapped_column(Integer, nullable=False, )
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=False, )
    email: Mapped[str] = mapped_column(String(50), nullable=False, )
    password: Mapped[str] = mapped_column(String(50), nullable=False, )
    is_active: Mapped[bool] = mapped_column(default=True,)