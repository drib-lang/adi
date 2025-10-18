from error import errors
from mem import Value, stack
from _token import Token, TokenType
from statement import Statement, StatementType


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.current_token: Token | None = None
        self.peek_token: Token | None = None

    def _are_parentheses_balanced(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{"}
        for ch in s:
            if ch in "({":
                stack.append(ch)
            elif ch in ")}":
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack

    def _parse_declaration_statement(self) -> Statement:
        tokens = [self.current_token]

        while True:
            if (
                self.peek_token.token_type == TokenType.SEMICOLON
                or self.peek_token.token_type == TokenType.EOF
            ):
                tokens.append(self.peek_token)
                break
            tokens.append(self.peek_token)
            self._next_token()

        s = " ".join(tok.literal for tok in tokens)

        if not self._are_parentheses_balanced(s):
            errors.append("syntax error: unbalanced parentheses")

        return Statement(StatementType.DECLARATION, tokens)

    def _parse_when_statement(self) -> Statement:
        tokens = [self.current_token]
        while True:
            s = "".join(tok.literal for tok in tokens)
            if (
                self.current_token.token_type == TokenType.RPAREN
                and self._are_parentheses_balanced(s)
            ):
                break
            tokens.append(self.peek_token)
            self._next_token()

        s = "".join(tok.literal for tok in tokens)

        if not self._are_parentheses_balanced(s):
            errors.append("syntax error: unbalanced parentheses")

        return Statement(StatementType.WHEN, tokens)

    def _next_token(self):
        self.current_token = self.peek_token
        self.peek_token = (
            self.tokens.pop(0) if self.tokens else Token(TokenType.EOF, "")
        )

    def parse_program(self) -> list[Statement]:
        self._next_token()
        self._next_token()
        statements = []

        while self.current_token.token_type != TokenType.EOF:
            if self.current_token.token_type == TokenType.VAL:
                statements.append(self._parse_declaration_statement())
            elif self.current_token.token_type == TokenType.WHEN:
                statements.append(self._parse_when_statement())
            self._next_token()
        return statements
