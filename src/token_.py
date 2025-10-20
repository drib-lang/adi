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


class Token:
    def __init__(self, token_type: str, literal: str):
        self.token_type = token_type
        self.literal = literal

    def __repr__(self):
        return f'{{"type": "{self.token_type}", "literal": "{self.literal}"}}'

    def __str__(self) -> str:
        return self.__repr__()
