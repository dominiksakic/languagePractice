from _token import make_token, Token

def scanner(source: str) -> list[Token]:
    tokens: list[Token] = []
    start: int = 0
    current: int = 0 
    line: int = 1

    def _is_at_end():
        return current >= len(source)

    def add_token(type_, lexeme, literal, line_):
        tokens.append(make_token(type_, lexeme, literal, line_))


    def scan_token() -> None:
        nonlocal current
        c = source[current]
        current += 1

        match c:
            case '(': add_token("LEFT_PAREN", "(", None, line)
            case ')': add_token("RIGHT_PAREN", "(", None, line)
            case '{': add_token("LEFT_BRACE", "(", None, line)
            case '}': add_token("RIGHT_BRACE", "(", None, line)
            case '+': add_token("PLUS", "+", None, line)
            case '-': add_token("MINUS", "-", None, line)
            case '.': add_token("DOT", ".", None, line)
            case ',': add_token("COMMA", ",", None, line)
            case ';': add_token("SEMICOLON", ";", None, line)
            case '*': add_token("STAR", "*", None, line)


    while not _is_at_end():
        start = current
        scan_token()

    tokens.append(make_token("EOF", "", None, line))
    return tokens

    




