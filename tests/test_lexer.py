import pytest
from json_parser.lexer import lex_string, _tokenize
from json_parser.models import JsonLexingError, JsonToken


def test_should_tokenize_left_bracket():
    token, _ = _tokenize("{", [])
    assert token is JsonToken.LEFT_CURLY_BRACKET


def test_should_tokenize_right_bracket():
    token, _ = _tokenize("}", [])
    assert token is JsonToken.RIGHT_CURLY_BRACKET


def test_should_tokenize_opening_quote():
    token, _ = _tokenize(r'"', [])
    assert token is JsonToken.OPENING_QUOTE


def test_should_tokenize_string_contents():
    token, buffer = _tokenize("a", [JsonToken.OPENING_QUOTE])
    assert token is JsonToken.STRING_CONTENT
    assert buffer == [JsonToken.OPENING_QUOTE, JsonToken.STRING_CONTENT]


def test_should_tokenize_entire_string():
    token, buffer = _tokenize(r'"', [JsonToken.OPENING_QUOTE, JsonToken.STRING_CONTENT])
    assert token is JsonToken.STRING
    assert len(buffer) == 0


def test_should_lex_random_string():
    tokens = lex_string(r'"try to tokenize me"')
    assert len(tokens) == 1
    assert tokens[0] is JsonToken.STRING


def test_should_not_lex_random_string_without_closing_quotes():
    with pytest.raises(JsonLexingError):
        lex_string(r'"try to tokenize me')
