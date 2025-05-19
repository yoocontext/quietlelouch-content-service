from domain.values.content import (
    NameValue,
    TitleValue,
    DescriptionValue,
    MediaTypeValue
)


class ContentValuesMapper:
    @staticmethod
    def get_name_value(name: str) -> NameValue:
        name_value = NameValue(value=name)
        return name_value

    @staticmethod
    def get_title_value(title: str) -> TitleValue:
        title_value = TitleValue(value=title)
        return title_value

    @staticmethod
    def get_description(description: str) -> DescriptionValue:
        description = DescriptionValue(value=description)
        return description

    @staticmethod
    def get_media_type(media_type: str) -> MediaTypeValue:
        media_type_value = MediaTypeValue(value=media_type)
        return media_type_value