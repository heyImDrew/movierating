from enum import Enum


class GenreEnum(Enum):
    ACTION = "Экшн"
    COMEDY = "Комедия"
    DRAMA = "Драма"
    FANTASY = "Фантастика"
    HORROR = "Хоррор"
    MYSTERY = "Мистическое"
    ROMANCE = "Романтика"
    THRILLER = "Триллер"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get(cls, name):
        for i in cls:
            if i.name == name:
                return i.value
        return None
