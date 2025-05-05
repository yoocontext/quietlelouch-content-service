from uuid import UUID, uuid4

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseOrm(DeclarativeBase):
    uid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)