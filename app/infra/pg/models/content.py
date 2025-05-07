from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseOrm
from .mixins import (
    IntPkMixin,
    UidPkMixin,
    CreateAtMixin,
    UpdateAtMixin
)

if TYPE_CHECKING:
    from .common import TagOrm

class MangaOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "mangas"

    title: Mapped[str]
    description: Mapped[str | None]
    pages_count: Mapped[int]

    pages: Mapped[list["PageOrm"]] = relationship(back_populates="manga")
    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_mangas_tags",
        back_populates="mangas",
    )
    extension: Mapped[str]

    extension_pk: Mapped[int] = mapped_column(ForeignKey("extensions.pk"))


class ImageOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "images"

    title: Mapped[str | None]
    description: Mapped[str | None]
    url: Mapped[str]
    height: Mapped[str]
    weight: Mapped[str]
    size: Mapped[int]
    extension: Mapped[str]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_images_tags",
        back_populates="images",
    )


class GifOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "gifs"

    title: Mapped[str | None]
    description: Mapped[str | None]
    url: Mapped[str]
    height: Mapped[int]
    weight: Mapped[int]
    size: Mapped[int]
    duration: Mapped[int]
    extension: Mapped[str]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_gifs_tags",
        back_populates="gifs",
    )


class VideoOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "videos"

    title: Mapped[str | None]
    description: Mapped[str | None]
    url: Mapped[str]
    height: Mapped[int]
    weight: Mapped[int]
    size: Mapped[int]
    duration: Mapped[int]
    extension: Mapped[str]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_videos_tags",
        back_populates="videos",
    )


class PageOrm(BaseOrm, IntPkMixin):
    __tablename__ = "pages"

    url: Mapped[str]
    height: Mapped[int]
    weight: Mapped[int]
    size: Mapped[int]

    manga: Mapped["MangaOrm"] = relationship(back_populates="pages")

    manga_uid: Mapped[UUID] = mapped_column(ForeignKey("mangas.uid"))