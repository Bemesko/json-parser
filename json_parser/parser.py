from json_parser.models import (
    EmptyJsonError,
    JsonParsingError,
    JsonToken,
    MismatchedCurlyBracesError,
)


def parse_json(tokens: list[JsonToken]) -> bool:
    try:
        ensure_json_is_not_empty(tokens)
        ensure_all_curly_brackets_are_matched(tokens)

        return True
    except JsonParsingError:
        return False


def ensure_all_curly_brackets_are_matched(tokens: list[JsonToken]) -> None:
    opening_brackets = tokens.count(JsonToken.LEFT_CURLY_BRACKET)
    closing_brackets = tokens.count(JsonToken.RIGHT_CURLY_BRACKET)

    if opening_brackets != closing_brackets:
        raise MismatchedCurlyBracesError(
            f"Expected {opening_brackets} opening curly brackets, but got {closing_brackets}"
        )


def ensure_json_is_not_empty(tokens: list[JsonToken]) -> None:
    if len(tokens) == 0:
        raise EmptyJsonError("Empty string is not valid JSON")
