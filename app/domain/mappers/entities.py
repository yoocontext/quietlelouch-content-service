from dataclasses import dataclass

from domain.entities.content import Image
from domain.values.content import (
    NameValue,
    TitleValue,
    DescriptionValue,
    MediaTypeValue,
)
from domain.mappers.values import ContentValuesMapper


@dataclass
class ContentEntityMapper:
    values_mapper: ContentValuesMapper

    def create_image(
        self,
        name: str,
        title: str | None,
        description: str | None,
        media_type: str,
    ) -> Image:
        name_value: NameValue = self.values_mapper.get_name_value(name=name)
        title_value: TitleValue | None = None
        description_value: DescriptionValue | None = None
        media_type_value: MediaTypeValue = self.values_mapper.get_media_type(media_type=media_type)

        if title:
            title_value: TitleValue = self.values_mapper.get_title_value(title=title)
        if description_value:
            description_value = self.values_mapper.get_description(description=description)

        image = Image(
            name=name_value,
            title=title_value,
            description=description_value,
            media_type=media_type_value,
        )
        return image