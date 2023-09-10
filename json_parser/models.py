from enum import Enum, auto


class JsonToken(Enum):
    LEFT_CURLY_BRACKET = auto()
    RIGHT_CURLY_BRACKET = auto()
    OPENING_QUOTE = auto()
    CLOSING_QUOTE = auto()
    STRING_CONTENT = auto()
    STRING = auto()
    WHITESPACE = auto()


class JsonLexingError(Exception):
    pass


class JsonParsingError(Exception):
    pass


class MismatchedCurlyBracesError(JsonParsingError):
    pass


class EmptyJsonError(JsonParsingError):
    pass
