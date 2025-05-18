import asyncio
from dataclasses import dataclass
from io import BytesIO

from fastapi import UploadFile
from PIL.ImageFile import ImageFile
from PIL import Image


from domain.logic.services import BaseService


@dataclass
class ImageMetadata:
    width: int
    height: int
    format: str


class GetPictureMetadataService(BaseService):
    """Работает с image and gif"""

    async def act(self, file: UploadFile) -> ImageMetadata:
        header: bytes = await self._get_header(file=file)
        image: ImageFile = await asyncio.to_thread(self._get_image, header)

        width, height = image.size
        image_format: str = image.format

        file.file.seek(0)

        resolution = ImageMetadata(width=width, height=height, format=image_format)
        return resolution

    @staticmethod
    def _get_image(header: bytes) -> ImageFile:
        image = Image.open(BytesIO(header))
        return image

    @staticmethod
    async def _get_header(file: UploadFile) -> bytes:
        header: bytes = await file.read(65536)
        return header
