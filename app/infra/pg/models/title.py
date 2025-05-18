from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.pg.models.common.base import BaseOrm
from infra.pg.models.content import MangaOrm, ImageOrm, GifOrm, VideoOrm
from infra.pg.models.common.mixins import IntPkMixin, CreateAtMixin, UpdateAtMixin


class TitleOrm(BaseOrm, IntPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "titles"

    name: Mapped[str] = mapped_column(unique=True)

    mangas: Mapped[list["MangaOrm"]] = relationship(
        back_populates="title",
    )
    images: Mapped[list["ImageOrm"]] = relationship(
        back_populates="title",
    )
    gifs: Mapped[list["GifOrm"]] = relationship(
        back_populates="title",
    )
    videos: Mapped[list["VideoOrm"]] = relationship(
        back_populates="title",
    )