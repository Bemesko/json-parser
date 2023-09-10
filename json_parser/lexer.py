from json_parser.models import JsonLexingError, JsonToken


def _tokenize(char: str, buffer: list[JsonToken]) -> tuple[JsonToken, list[JsonToken]]:
    match char:
        case "{":
            return JsonToken.LEFT_CURLY_BRACKET, []
        case "}":
            return JsonToken.RIGHT_CURLY_BRACKET, []
        case ",":
            return JsonToken.COMMA, []
        case ":":
            return JsonToken.COLON, []
        case '"' if len(buffer) == 0:
            return JsonToken.OPENING_QUOTE, [JsonToken.OPENING_QUOTE]
        case '"' if is_unclosed_string(buffer):
            return JsonToken.STRING, []
        case char if starts_with_opening_quote(buffer):
            buffer.append(JsonToken.STRING_CONTENT)
            return JsonToken.STRING_CONTENT, buffer
        case " " | "\n" | "\r" | "\t":
            return JsonToken.WHITESPACE, []
        case _:
            raise JsonLexingError()


def starts_with_opening_quote(buffer: list[JsonToken]) -> bool:
    try:
        return buffer[0] is JsonToken.OPENING_QUOTE
    except IndexError:
        return False


def is_unclosed_string(buffer: list[JsonToken]) -> bool:
    return len(buffer) > 1 and starts_with_opening_quote(buffer)


def lex_string(string: str) -> list[JsonToken]:
    char_stack = list(string)
    char_stack.reverse()

    buffer = []
    tokens: list[JsonToken] = []

    while char_stack:
        current_char = char_stack.pop()

        current_token, current_buffer = _tokenize(current_char, buffer)

        if len(current_buffer) > 0:
            buffer.extend(current_buffer)
        else:
            buffer.clear()
            tokens.append(current_token)

    if len(buffer) != 0:
        raise JsonLexingError()

    return tokens
