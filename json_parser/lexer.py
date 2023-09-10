from json_parser.models import JsonLexingError, JsonToken


def convert_to_token(char: str) -> JsonToken:
    match char:
        case "{":
            return JsonToken.LEFT_CURLY_BRACKET
        case "}":
            return JsonToken.RIGHT_CURLY_BRACKET
        case _:
            raise JsonLexingError()


def lex_string(string: str) -> list[JsonToken]:
    tokens = []
    for char in string:
        token = convert_to_token(char)
        tokens.append(token)
    return tokens
