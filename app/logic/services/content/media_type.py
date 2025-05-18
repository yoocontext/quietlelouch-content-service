from domain.entities.content import MediaType
from domain.logic.services import BaseService
from domain.values.exceptions import MediaTypeNotExistException


class GetMediaTypeService(BaseService):
    async def act(self, format_type: str) -> MediaType:
        content_type: str = self._get_content_type(format_type=format_type)

        try:
            media_type: MediaType = MediaType(content_type)
        except ValueError:
            raise MediaTypeNotExistException(media_type=content_type)

        return media_type

    @staticmethod
    def _get_content_type(format_type: str) -> str:
        format_type = format_type.lower()
        content_type = None

        if format_type in ("jpeg", "png", "gif"):
            content_type = fr"image/{content_type}"
        elif format_type in ("mp4",):
            content_type = fr"video/{content_type}"

        return content_type

