from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.pg.models import BaseOrm
from infra.pg.models.content import MangaOrm, ImageOrm, GifOrm, VideoOrm
from infra.pg.models.common.mixins import UidPkMixin, CreateAtMixin, UpdateAtMixin


class AuthorOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "authors"
    name: Mapped[str] = mapped_column(unique=True)
    bio: Mapped[str | None]

    mangas: Mapped[list["MangaOrm"]] = relationship(
        back_populates="author",
    )
    images: Mapped[list["ImageOrm"]] = relationship(
        back_populates="author",
    )
    gifs: Mapped[list["GifOrm"]] = relationship(
        back_populates="author",
    )
    videos: Mapped[list["VideoOrm"]] = relationship(
        back_populates="author",
    )
