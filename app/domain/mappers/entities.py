from dataclasses import dataclass

from domain.entities.content import Image
from domain.values.content.common import (
    NameValue,
    TitleValue,
    DescriptionValue,
    MediaTypeValue,
)
from domain.mappers.values import ContentValuesMapper
from domain.values.content.image import ImageSizeValue


@dataclass
class ContentEntityMapper:
    values_mapper: ContentValuesMapper

    def create_image(
        self,
        name: str,
        title: str | None,
        description: str | None,
        media_type: str,
        size: int,
        width: int,
        height: int,
    ) -> Image:
        name_value: NameValue = self.values_mapper.get_name_value(name=name)
        size_value: ImageSizeValue = self.values_mapper.get_size(size=size)
        media_type_value: MediaTypeValue = self.values_mapper.get_media_type(media_type=media_type)
        title_value: TitleValue | None = None
        description_value: DescriptionValue | None = None

        if title:
            title_value: TitleValue = self.values_mapper.get_title_value(title=title)
        if description_value:
            description_value = self.values_mapper.get_description(description=description)

        image = Image(
            name=name_value,
            title=title_value,
            description=description_value,
            media_type=media_type_value,
            size=size_value,
            width=width,
            height=height,
        )
        return image