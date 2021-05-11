from enum import Enum


class StatusEnum(Enum):
    ENABLED = "Активен"
    DISABLED = "Заблокирован"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
