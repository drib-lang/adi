class TokenType:
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    # identifiers + literals
    ASSIGN = "ASSIGN"
    IDENTIFIER = "IDENTIFIER"

    # delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # keywords and types (true, false, string)
    FUNCTION = "FUNCTION"
    VAL = "VAL"
    RETURN = "RETURN"
    WHEN = "WHEN"
    OTHERWISE = "OTHERWISE"
    TRUE = "TRUE"
    FALSE = "FALSE"
    STRING = "STRING"
    NIL = "NIL"

    # loop-related
    LOOP = "LOOP"
    NEXT = "NEXT"
    OUT = "OUT"


class Token:
    def __init__(self, token_type: str, literal: str):
        self.token_type = token_type
        self.literal = literal

    def __repr__(self):
        return f'{"token_type": "{self.token_type}", "literal": "{self.literal}"}'

    def __str__(self) -> str:
        return self.__repr__()
