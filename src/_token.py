class TokenType:
    TT_EOF = "EOF"
    TT_ILLEGAL = "ILLEGAL"

    # identifiers + literals
    TT_ASSIGN = "ASSIGN"
    TT_IDENTIFIER = "IDENTIFIER"

    # delimiters
    TT_COMMA = "COMMA"
    TT_SEMICOLON = "SEMICOLON"

    TT_LPAREN = "LPAREN"
    TT_RPAREN = "RPAREN"
    TT_LBRACE = "LBRACE"
    TT_RBRACE = "RBRACE"
    TT_LBRACKET = "LBRACKET"
    TT_RBRACKET = "RBRACKET"

    # keywords
    TT_FUNCTION = "FUNCTION"
    TT_VAL = "VAL"
    TT_RETURN = "RETURN"
    TT_IF = "IF"
    TT_ELSE = "ELSE"
    TT_TRUE = "TRUE"
    TT_FALSE = "FALSE"


class Token:
    def __init__(self, type_: str, literal: str):
        self.type = type_
        self.literal = literal

    def __repr__(self):
        return f'{{"type": "{self.type}", "literal": "{self.literal}"}}'

    def __str__(self):
        return f'{{"type": "{self.type}", "literal": "{self.literal}"}}'
