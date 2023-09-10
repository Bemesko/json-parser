import pytest
import json_parser.models as models
import json_parser.parser as parser
import json_parser.lexer as lexer


def test_should_raise_mismatched_curly_braces_error():
    test_tokens = lexer.lex_string(r"{{}")

    with pytest.raises(models.MismatchedCurlyBracesError):
        parser.ensure_all_curly_brackets_are_matched(test_tokens)


def test_should_not_raise_mismatched_curly_braces_error():
    test_tokens = lexer.lex_string(r"{{}}")

    parser.ensure_all_curly_brackets_are_matched(test_tokens)


def test_should_raise_empty_json_error():
    test_tokens = lexer.lex_string(r"")

    with pytest.raises(models.EmptyJsonError):
        parser.ensure_json_is_not_empty(test_tokens)


def test_should_not_raise_empty_json_error():
    test_tokens = lexer.lex_string(r"{}")

    parser.ensure_json_is_not_empty(test_tokens)
