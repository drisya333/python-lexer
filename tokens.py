from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    IDENT = auto()

    PLUS = auto()
    MINUS = auto()
    MUL = auto()
    DIV = auto()
    ASSIGN = auto()

    LPAREN = auto()
    RPAREN = auto()

    EOF = auto()


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"{self.type.name}({self.value})"
        return f"{self.type.name}"
