from token_ import Token
from token_ import TokenType


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.position = 0  # current position in text (points to current char)
        self.read_position = 0  # current reading position in text (after current char)
        self.ch = ""  # current char under examination
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.text):
            self.ch = "\0"
        else:
            self.ch = self.text[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def skip_whitespace(self):
        while self.ch in " \t\n\r":
            self.read_char()

    def is_letter(self, ch: str):
        return ch.isalpha() or ch == "_"

    def read_identifier(self):
        start = self.position
        while self.is_letter(self.ch):
            self.read_char()
        return self.text[start : self.position]

    def read_string(self):
        start = self.position + 1
        while True:
            self.read_char()
            if self.ch == '"' or self.ch == "\0":
                break
        return f'"{self.text[start : self.position]}"'

    def lookup_ident(self, ident: str):
        keywords = {
            "fun": TokenType.FUNCTION,
            "val": TokenType.VAL,
            "return": TokenType.RETURN,
            "when": TokenType.WHEN,
            "otherwise": TokenType.OTHERWISE,
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "nil": TokenType.NIL,
        }
        return keywords.get(ident, TokenType.IDENTIFIER)

    def next_token(self):
        self.skip_whitespace()
        tok = None

        match self.ch:
            case "=":
                tok = Token(TokenType.ASSIGN, self.ch)
            case ";":
                tok = Token(TokenType.SEMICOLON, self.ch)
            case "(":
                tok = Token(TokenType.LPAREN, self.ch)
            case ")":
                tok = Token(TokenType.RPAREN, self.ch)
            case ",":
                tok = Token(TokenType.COMMA, self.ch)
            case "{":
                tok = Token(TokenType.LBRACE, self.ch)
            case "}":
                tok = Token(TokenType.RBRACE, self.ch)
            case '"':
                tok = Token(TokenType.STRING, self.read_string())
            case "\0":
                tok = Token(TokenType.EOF, "")
            case _:
                if self.is_letter(self.ch):
                    literal = self.read_identifier()
                    tok = Token(self.lookup_ident(literal), literal)
                    return tok
                else:
                    tok = Token(TokenType.ILLEGAL, self.ch)
        self.read_char()
        return tok

    def tokenize(self):
        tokens = []
        while True:
            tok = self.next_token()
            tokens.append(tok)
            if tok.token_type == TokenType.EOF:
                break
        return tokens
