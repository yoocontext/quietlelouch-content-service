from domain.values.content.common import MediaType
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
    def _get_content_type(format_type: str) -> str | None:
        format_type = format_type.lower()


        if format_type == "jpg":
            return "image/jpeg"
        elif format_type in ("jpeg", "png", "gif"):
            return f"image/{format_type}"
        elif format_type == "mp4":
            return f"video/{format_type}"

