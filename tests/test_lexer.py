import pytest
from json_parser.lexer import convert_to_token
from json_parser.models import JsonLexingError, JsonToken


def test_should_tokenize_left_bracket():
    assert convert_to_token("{") is JsonToken.LEFT_CURLY_BRACKET


def test_should_tokenize_right_bracket():
    assert convert_to_token("}") is JsonToken.RIGHT_CURLY_BRACKET


def test_should_raise_error_if_cannot_tokenize():
    with pytest.raises(JsonLexingError):
        convert_to_token("?")
