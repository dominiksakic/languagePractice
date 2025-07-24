from _token import make_token, Token
from report import error

def scanner(source: str) -> list[Token]:
    tokens: list[Token] = []
    start: int = 0
    current: int = 0 
    line: int = 1

    def _is_at_end():
        return current >= len(source)

    def add_token(type_, lexeme=None, literal=None):
        text = source[start:current] if lexeme is None else lexeme
        tokens.append(make_token(type_, text, literal, line))

    def match(expected: str) -> bool:
        nonlocal current
        if _is_at_end():
            return False
        if source[current] != expected:
            return False
        current += 1
        return True


    def scan_token() -> None:
        nonlocal current

        c = source[current]
        current += 1

        match c:
            case '(': add_token("LEFT_PAREN")
            case ')': add_token("RIGHT_PAREN")
            case '{': add_token("LEFT_BRACE")
            case '}': add_token("RIGHT_BRACE")
            case '+': add_token("PLUS")
            case '-': add_token("MINUS")
            case '.': add_token("DOT")
            case ',': add_token("COMMA")
            case ';': add_token("SEMICOLON")
            case '*': add_token("STAR")
            case '!': 
                add_token("BANG_EQUAL" if match('=') else 'BANG')
            case '=': 
                add_token("EQUAL_EQUAL" if match('=') else 'EQUAL')
            case '<': 
                add_token("LESS_EQUAL" if match('=') else 'LESS')
            case '>': 
                add_token("GREATER_EQUAL" if match('=') else 'GREATER')
            case _ : error(line, "Unexpected character.")


    while not _is_at_end():
        start = current
        scan_token()

    tokens.append(make_token("EOF", "", None, line))
    return tokens

    




