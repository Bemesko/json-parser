from enum import Enum, auto


class JsonToken(Enum):
    LEFT_CURLY_BRACKET = auto()
    RIGHT_CURLY_BRACKET = auto()
    WHITESPACE = auto()


class JsonLexingError(Exception):
    pass


class JsonParsingError(Exception):
    pass


class MismatchedCurlyBracesError(JsonParsingError):
    pass


class EmptyJsonError(JsonParsingError):
    pass
