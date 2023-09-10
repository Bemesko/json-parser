from json_parser.core import parse


def test_valid_json_with_one_atrribute():
    test_json = r'{"key": "value"}'

    assert parse(test_json) is True
