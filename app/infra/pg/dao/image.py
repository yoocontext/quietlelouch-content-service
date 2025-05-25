from uuid import UUID

from sqlalchemy import select, delete
from sqlalchemy.orm import joinedload, selectinload

from infra.pg.dao.base import BaseDao
from infra.pg.dao.exceptions import ObjectNotFoundException
from infra.pg.models import ImageOrm


class ImageDao(BaseDao):
    async def get(self, uid: UUID) -> ImageOrm:
        result = await self.session.execute(
            select(ImageOrm)
            .where(ImageOrm.uid == uid)
            .options(
                joinedload(ImageOrm.title),
                joinedload(ImageOrm.author),
                joinedload(ImageOrm.language),
                selectinload(ImageOrm.tags),
                selectinload(ImageOrm.access_roles),
            )
        )
        image_orm: ImageOrm | None = result.scalar_one_or_none()

        if image_orm:
            return image_orm
        else:
            raise ObjectNotFoundException(required_obj=uid)


    async def delete(self, uid: UUID) -> None:
        result = await self.session.execute(
            delete(ImageOrm)
            .where(ImageOrm.uid == uid)
            .returning(ImageOrm.uid)
        )
        deleted_uid = result.scalar_one_or_none()

        if not deleted_uid:
            raise ObjectNotFoundException(required_obj=deleted_uid)
