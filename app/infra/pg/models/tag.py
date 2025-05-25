from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infra.pg.models.common.base import BaseOrm
from infra.pg.models.content import MangaOrm, ImageOrm, GifOrm, VideoOrm
from infra.pg.models.common.mixins import IntPkMixin, UidPkMixin, CreateAtMixin, UpdateAtMixin


class TagOrm(BaseOrm, UidPkMixin, CreateAtMixin, UpdateAtMixin):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]

    mangas: Mapped[list["MangaOrm"]] = relationship(
        secondary="a_manga_tags",
        back_populates="tags",
    )
    images: Mapped[list["ImageOrm"]] = relationship(
        secondary="a_images_tags",
        back_populates="tags",
    )
    gifs: Mapped[list["GifOrm"]] = relationship(
        secondary="a_gifs_tags",
        back_populates="tags",
    )
    videos: Mapped[list["VideoOrm"]] = relationship(
        secondary="a_videos_tags",
        back_populates="tags",
    )



class VideosTagsOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_videos_tags"

    gif_uid: Mapped[UUID] = mapped_column(ForeignKey("videos.uid", ondelete="CASCADE"), primary_key=True)
    tags_pk: Mapped[int] = mapped_column(ForeignKey("tags.uid", ondelete="CASCADE"),  primary_key=True)


class GifsTagsOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_gifs_tags"

    gif_uid: Mapped[UUID] = mapped_column(ForeignKey("gifs.uid", ondelete="CASCADE"), primary_key=True)
    tag_pk: Mapped[int] = mapped_column(ForeignKey("tags.uid", ondelete="CASCADE"), primary_key=True)


class ImagesTagsOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_images_tags"

    image_uid: Mapped[UUID] = mapped_column(ForeignKey("images.uid", ondelete="CASCADE"), primary_key=True)
    tag_pk: Mapped[int] = mapped_column(ForeignKey("tags.uid", ondelete="CASCADE"), primary_key=True)


class MangasTagsOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_manga_tags"

    manga_uid: Mapped[UUID] = mapped_column(ForeignKey("mangas.uid", ondelete="CASCADE"), primary_key=True)
    tag_pk: Mapped[int] = mapped_column(ForeignKey("tags.uid", ondelete="CASCADE"), primary_key=True)
