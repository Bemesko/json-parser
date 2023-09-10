from json_parser.core import parse


def test_should_parse_empty_object():
    assert parse(r"{}") is True


def test_should_not_parse_missing_closing_bracket():
    assert parse(r"{") is False


def test_should_not_parse_empty_string():
    assert parse(r"") is False
