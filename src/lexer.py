from _token import Token
from _token import TokenType


class Lexer:
    def __init__(self, _input: str):
        self.input = _input
        self.position = 0  # current position in input (points to current char)
        self.read_position = 0  # current reading position in input (after current char)
        self.ch = ""  # current char under examination
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = "\0"
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def skip_whitespace(self):
        while self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
            self.read_char()

    def is_letter(self, ch: str):
        return "a" <= ch <= "z" or "A" <= ch <= "Z" or ch == "_"

    def read_identifier(self):
        pos = self.position
        while self.is_letter(self.ch):
            self.read_char()
        return self.input[pos : self.position]

    def lookup_ident(self, ident: str):
        keywords = {
            "fun": TokenType.TT_FUNCTION,
            "val": TokenType.TT_VAL,
            "return": TokenType.TT_RETURN,
            "if": TokenType.TT_IF,
            "else": TokenType.TT_ELSE,
            "true": TokenType.TT_TRUE,
            "false": TokenType.TT_FALSE,
        }
        return keywords.get(ident, TokenType.TT_IDENTIFIER)

    def next_token(self):
        self.skip_whitespace()
        tok = None

        match self.ch:
            case "=":
                tok = Token(TokenType.TT_ASSIGN, self.ch)
            case ";":
                tok = Token(TokenType.TT_SEMICOLON, self.ch)
            case "(":
                tok = Token(TokenType.TT_LPAREN, self.ch)
            case ")":
                tok = Token(TokenType.TT_RPAREN, self.ch)
            case ",":
                tok = Token(TokenType.TT_COMMA, self.ch)
            case "{":
                tok = Token(TokenType.TT_LBRACE, self.ch)
            case "}":
                tok = Token(TokenType.TT_RBRACE, self.ch)
            case "\0":
                tok = Token(TokenType.TT_EOF, "")
            case _:
                if self.is_letter(self.ch):
                    literal = self.read_identifier()
                    tok = Token(self.lookup_ident(literal), literal)
                    return tok
                else:
                    tok = Token(TokenType.TT_ILLEGAL, self.ch)

        self.read_char()
        return tok
