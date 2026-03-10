from sqlalchemy import String, Integer, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

class JobsModel(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(150))
    salary: Mapped[float]
    office_address: Mapped[str] = mapped_column(String(50))
    requirements: Mapped[list] = mapped_column(JSONB)
    is_active: Mapped[bool] = mapped_column(default=True)
    email: Mapped[str] = mapped_column(String(50))
    cell_count: Mapped[int] = mapped_column(Integer, default=0)
