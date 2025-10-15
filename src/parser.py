from mem import Value, stack
from _token import Token, TokenType


# class Pythonizer:
#     @staticmethod
#     def check_stack(stack, token: Token):
#         levels = len(stack)

#         for level in range(0, levels):
#             for val in stack[level]:
#                 if val.name == token.literal:
#                     print(val.value)
#                     return True

#         print(f"{token.literal} is not defined")
#         return False

#     @staticmethod
#     def pythonize(tokens: list[Token]) -> list[str]:
#         python = []
#         indent_level = 0

#         for token in tokens:
#             if token.token_type == TokenType.IF:
#                 python.append("    " * indent_level + f"if {token.literal}:")
#                 indent_level += 1

#         return python


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.current_token: Token | None = None
        self.peek_token: Token | None = None
        self.valid_following_tokens = {
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
        }

    def parse_program(self):
        self._next_token()
        self._next_token()

        while self.current_token.token_type != TokenType.EOF:
            print(self.current_token)
            self._next_token()

        print("Parsing complete.")

    def _parse_val_statement(self):
        pass

    def _next_token(self):
        self.current_token = self.peek_token
        self.peek_token = (
            self.tokens.pop(0) if self.tokens else Token(TokenType.EOF, "")
        )
