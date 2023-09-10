from json_parser.lexer import lex_string
from json_parser.models import JsonLexingError
from json_parser.parser import parse_json


def parse(json_string: str) -> bool:
    try:
        tokens = lex_string(json_string)
    except JsonLexingError:
        return False

    return parse_json(tokens)
