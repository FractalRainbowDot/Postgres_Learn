from sqlalchemy import String, Integer, Enum, Float
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

class Works(Base):
    __tablename__ = "jobs"

    jobs_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(150))
    salary: Mapped[float]
    office_address: Mapped[str] = mapped_column(String(50))
    requirements: Mapped[str] = mapped_column(String(150))
    is_active: Mapped[bool] = mapped_column(default=True)
    email: Mapped[str] = mapped_column(String(50))
    cell_count: Mapped[int] = mapped_column(Integer, default=0)
