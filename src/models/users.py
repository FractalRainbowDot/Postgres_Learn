from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from base import Base

class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, )
    surname: Mapped[str] = mapped_column(String(50), nullable=False, )
    age: Mapped[int] = mapped_column(Integer, nullable=False, )