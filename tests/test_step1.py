from json_parser.json_parser import parse_json


def test_should_parse_empty_object():
    assert parse_json(r"{}") is True
