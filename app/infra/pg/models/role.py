from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from infra.pg.models import BaseOrm
from infra.pg.models.content import MangaOrm, ImageOrm, GifOrm, VideoOrm
from infra.pg.models.common.mixins import IntPkMixin


class RoleOrm(BaseOrm, IntPkMixin):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]

    mangas: Mapped[list["MangaOrm"]] = relationship(
        secondary="a_mangas_roles",
        back_populates="access_roles",
    )
    images: Mapped[list["ImageOrm"]] = relationship(
        secondary="a_images_roles",
        back_populates="access_roles",
    )
    gifs: Mapped[list["GifOrm"]] = relationship(
        secondary="a_gifs_roles",
        back_populates="access_roles",
    )
    videos: Mapped[list["VideoOrm"]] = relationship(
        secondary="a_videos_roles",
        back_populates="access_roles",
    )


class MangasRolesOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_manga_roles"

    manga_uid: Mapped[UUID] = mapped_column(ForeignKey("mangas.uid"), primary_key=True)
    role_pk: Mapped[int] = mapped_column(ForeignKey("roles.pk"), primary_key=True)


class ImagesRolesOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_images_roles"

    image_uid: Mapped[UUID] = mapped_column(ForeignKey("images.uid"), primary_key=True)
    role_pk: Mapped[int] = mapped_column(ForeignKey("roles.pk"), primary_key=True)


class GifsRolesOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_gifs_roles"

    gif_uid: Mapped[UUID] = mapped_column(ForeignKey("gifs.uid"), primary_key=True)
    role_pk: Mapped[int] = mapped_column(ForeignKey("roles.pk"), primary_key=True)


class VideosRolesOrm(BaseOrm, IntPkMixin):
    __tablename__ = "a_videos_roles"

    gif_uid: Mapped[UUID] = mapped_column(ForeignKey("videos.uid"), primary_key=True)
    role_pk: Mapped[int] = mapped_column(ForeignKey("roles.pk"), primary_key=True)