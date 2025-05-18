from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.pg.models.author import AuthorOrm
from infra.pg.models.common.base import BaseOrm
from infra.pg.models.common.mixins import (
    UidPkMixin,
    CreateAtMixin,
    UpdateAtMixin,
)
from infra.pg.models.title import TitleOrm
from infra.pg.types import UserUid, SizeInBytes

if TYPE_CHECKING:
    from .language import LanguageOrm
    from .role import RoleOrm
    from .tag import TagOrm


class MangaOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "mangas"

    name: Mapped[str]
    description: Mapped[str | None]
    pages_count: Mapped[int]
    media_type: Mapped[str]
    nsfw: Mapped[bool]
    added_by: Mapped[UserUid]
    translated_by: Mapped[UserUid | None]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_mangas_tags",
        back_populates="mangas",
    )
    access_roles: Mapped[list["RoleOrm"]] = relationship(
        secondary="a_mangas_roles",
        back_populates="mangas",
    )
    pages: Mapped[list["PageOrm"]] = relationship(back_populates="manga")
    title: Mapped["TitleOrm"] = relationship(back_populates="mangas")
    author: Mapped["AuthorOrm"] = relationship(back_populates="mangas")
    language: Mapped["LanguageOrm"] = relationship(back_populates="mangas")

    title_pk: Mapped[int | None] = mapped_column(ForeignKey("titles.pk"))
    author_uid: Mapped[UUID | None] = mapped_column(ForeignKey("authors.uid"))
    language_pk: Mapped[int] = mapped_column(ForeignKey("languages.pk"))


class ImageOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "images"

    name: Mapped[str]
    description: Mapped[str | None]
    height: Mapped[int]
    width: Mapped[int]
    size: Mapped[SizeInBytes]
    media_type: Mapped[str]
    nsfw: Mapped[bool]
    added_by: Mapped[UserUid]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_images_tags",
        back_populates="images",
    )
    access_roles: Mapped[list["RoleOrm"]] = relationship(
        secondary="a_images_roles",
        back_populates="images"
    )
    title: Mapped["TitleOrm"] = relationship(back_populates="images")
    author: Mapped["AuthorOrm"] = relationship(back_populates="images")
    language: Mapped["LanguageOrm"] = relationship(back_populates="images")

    author_uid: Mapped[UUID | None] = mapped_column(ForeignKey("authors.uid"))
    title_pk: Mapped[int | None] = mapped_column(ForeignKey("titles.pk"))
    language_pk: Mapped[int] = mapped_column(ForeignKey("languages"))


class GifOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "gifs"

    name: Mapped[str]
    description: Mapped[str | None]
    height: Mapped[int]
    width: Mapped[int]
    size: Mapped[SizeInBytes]
    duration: Mapped[int]
    media_type: Mapped[str]
    nsfw: Mapped[bool]
    added_by: Mapped[UserUid]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_gifs_tags",
        back_populates="gifs",
    )
    access_roles: Mapped[list["RoleOrm"]] = relationship(
        secondary="a_gifs_roles",
        back_populates="gifs"
    )
    title: Mapped["TitleOrm"] = relationship(back_populates="gifs")
    author: Mapped["AuthorOrm"] = relationship(back_populates="gifs")
    language: Mapped["LanguageOrm"] = relationship(back_populates="gifs")

    author_uid: Mapped[UUID | None] = mapped_column(ForeignKey("authors.uid"))
    title_pk: Mapped[int | None] = mapped_column(ForeignKey("titles.pk"))
    language_pk: Mapped[int] = mapped_column(ForeignKey("languages"))


class VideoOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "videos"

    name: Mapped[str]
    description: Mapped[str | None]
    height: Mapped[int]
    width: Mapped[int]
    size: Mapped[SizeInBytes]
    duration: Mapped[int]
    media_type: Mapped[str]
    nsfw: Mapped[bool]
    added_by: Mapped[UserUid]

    tags: Mapped[list["TagOrm"]] = relationship(
        secondary="a_videos_tags",
        back_populates="videos",
    )
    access_roles: Mapped[list["RoleOrm"]] = relationship(
        secondary="a_videos_roles",
        back_populates="videos"
    )
    title: Mapped["TitleOrm"] = relationship(back_populates="videos")
    author: Mapped["AuthorOrm"] = relationship(back_populates="videos")
    language: Mapped["LanguageOrm"] = relationship(back_populates="videos")

    author_uid: Mapped[UUID | None] = mapped_column(ForeignKey("authors.uid"))
    title_pk: Mapped[int | None] = mapped_column(ForeignKey("titles.pk"))
    language_pk: Mapped[int] = mapped_column(ForeignKey("languages"))


class PageOrm(BaseOrm, UidPkMixin):
    __tablename__ = "pages"

    height: Mapped[int]
    width: Mapped[int]
    size: Mapped[SizeInBytes]
    page_number: Mapped[int]

    manga: Mapped["MangaOrm"] = relationship(back_populates="pages")

    manga_uid: Mapped[UUID] = mapped_column(ForeignKey("mangas.uid"))
