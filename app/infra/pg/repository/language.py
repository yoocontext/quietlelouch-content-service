from uuid import UUID

from sqlalchemy import select

from infra.pg.models import LanguageOrm
from infra.pg.repository.common.base import BaseRepository
from infra.pg.repository.common.errors import ObjectNotFoundException, MissingRequiredField


class LanguageRepository(BaseRepository):
    async def get_by_uid(self, uid: UUID) -> LanguageOrm:
        language_orm: LanguageOrm | None = await self.session.get(LanguageOrm, uid)
        if language_orm:
            return language_orm
        else:
            raise ObjectNotFoundException(required_obj=uid)

    async def get_by_name(self, name: str) -> LanguageOrm:
        result = await self.session.execute(
            select(LanguageOrm)
            .where(LanguageOrm.name == name)
        )
        language_orm: LanguageOrm | None = result.scalar_one_or_none()
        if language_orm:
            return language_orm
        else:
            raise MissingRequiredField(required_field=name)
