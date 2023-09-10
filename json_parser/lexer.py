from json_parser.models import JsonLexingError, JsonToken


def convert_to_token(char: str) -> JsonToken:
    match char:
        case "{":
            return JsonToken.LEFT_CURLY_BRACKET
        case "}":
            return JsonToken.RIGHT_CURLY_BRACKET
        case _:
            raise JsonLexingError()


def tokenize(char: str, buffer: list[JsonToken]) -> tuple[JsonToken, list[JsonToken]]:
    match char:
        case "{":
            return JsonToken.LEFT_CURLY_BRACKET, []
        case "}":
            return JsonToken.RIGHT_CURLY_BRACKET, []
        case '"' if len(buffer) == 0:
            return JsonToken.OPENING_QUOTE, [JsonToken.OPENING_QUOTE]
        case '"' if buffer[0] is JsonToken.OPENING_QUOTE and len(buffer) > 1:
            return JsonToken.STRING, []
        case char if buffer[0] is JsonToken.OPENING_QUOTE:
            buffer.append(JsonToken.STRING_CONTENT)
            return JsonToken.STRING_CONTENT, buffer
        case _:
            raise JsonLexingError()


def lex_string(string: str) -> list[JsonToken]:
    char_stack = list(string)
    char_stack.reverse()

    buffer = []
    tokens: list[JsonToken] = []

    while char_stack:
        current_char = char_stack.pop()

        current_token, current_buffer = tokenize(current_char, buffer)

        if len(current_buffer) > 0:
            buffer.extend(current_buffer)
        else:
            buffer.clear()
            tokens.append(current_token)

    if len(buffer) != 0:
        raise JsonLexingError()

    return tokens
