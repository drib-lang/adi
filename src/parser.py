from mem import Value, stack
from _token import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.current_token: Token | None = None
        self.peek_token: Token | None = None
        self.following_tokens = {
            TokenType.VAL: [TokenType.IDENTIFIER],
            TokenType.IDENTIFIER: [
                TokenType.ASSIGN,  # a =
                TokenType.LPAREN,  # a (
                TokenType.COMMA,  # a, b
                TokenType.RPAREN,  # a)
                TokenType.SEMICOLON,  # a;
            ],
            TokenType.ASSIGN: [
                TokenType.IDENTIFIER,  # a = b
                TokenType.STRING,  # a = "string"
                TokenType.TRUE,  # a = true
                TokenType.FALSE,  # a = false
                TokenType.NIL,  # a = nil
            ],
            TokenType.STRING: [TokenType.SEMICOLON, TokenType.COMMA, TokenType.RPAREN],
            TokenType.TRUE: [TokenType.SEMICOLON, TokenType.COMMA, TokenType.RPAREN],
            TokenType.FALSE: [TokenType.SEMICOLON, TokenType.COMMA, TokenType.RPAREN],
            TokenType.NIL: [TokenType.SEMICOLON, TokenType.COMMA],
        }

    def _validate_following_token(self):
        valid_tokens = self.following_tokens[self.current_token.token_type]
        if self.peek_token.token_type not in valid_tokens:
            print(f"unexpected {self.peek_token.token_type} token")
            return False
        return True

    def _parse_val_statement(self):
        tokens = [self.current_token]
        while self.peek_token.token_type != TokenType.EOF:
            print(f"Current token: {self.current_token}")
            if self._validate_following_token():
                tokens.append(self.peek_token)
                self._next_token()
            else:
                print("syntax error in val statement")
                return

    def _next_token(self):
        self.current_token = self.peek_token
        self.peek_token = (
            self.tokens.pop(0) if self.tokens else Token(TokenType.EOF, "")
        )

    def parse_program(self):
        self._next_token()
        self._next_token()

        while self.current_token.token_type != TokenType.EOF:
            print(f"Current token: {self.current_token}")
            if self.current_token == TokenType.VAL:
                self._parse_val_statement()
            self._next_token()

        print("Parsing complete.")
