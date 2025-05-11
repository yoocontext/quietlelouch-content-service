from sqlalchemy.orm import Mapped, relationship

from infra.pg.models import BaseOrm
from infra.pg.models.content import MangaOrm, ImageOrm, GifOrm, VideoOrm
from infra.pg.models.common.mixins import IntPkMixin


class LanguageOrm(BaseOrm, IntPkMixin):
    __tablename__ = "languages"

    name: Mapped[str]
    description: Mapped[str | None]

    mangas: Mapped[list["MangaOrm"]] = relationship(
        back_populates="language",
    )
    images: Mapped[list["ImageOrm"]] = relationship(
        back_populates="language",
    )
    gifs: Mapped[list["GifOrm"]] = relationship(
        back_populates="language",
    )
    videos: Mapped[list["VideoOrm"]] = relationship(
        back_populates="language",
    )
