from dataclasses import dataclass

@dataclass
class Token:
    type: str
    lexeme: str
    literal: object
    line: int

def make_token(type_, lexeme, literal, line_) -> dict:
    return Token(type_, lexeme, literal, line_)
