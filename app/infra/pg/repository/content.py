from uuid import UUID

from infra.pg.models.content import (
    MangaOrm,
    ImageOrm,
    GifOrm,
    VideoOrm
)
from infra.pg.repository.base import BaseRepository
from infra.pg.repository.errors import ObjectNotFoundException


class MangaRepository(BaseRepository):
    async def get_by_uid(self, uid: UUID) -> MangaOrm:
        manga: MangaOrm | None = await self.session.get(MangaOrm, uid)
        if manga:
            return manga
        else:
            raise ObjectNotFoundException(required_obj=uid)
