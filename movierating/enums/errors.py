from enum import Enum


class ErrorsEnum(Enum):
    USER_NOT_FOUND = "UNF"
    USER_ALREADY_EXISTS = "UAE"
    INCORRECT_INPUT = "II"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
