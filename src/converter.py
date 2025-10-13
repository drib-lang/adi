from mem import Value, stack
from _token import Token, TokenType


class Pythonizer:
    @staticmethod
    def check_stack(stack, token: Token):
        levels = len(stack)

        for level in range(0, levels):
            for val in stack[level]:
                if val.name == token.literal:
                    print(val.value)
                    return True

        print(f"{token.literal} is not defined")
        return False

    @staticmethod
    def pythonize(tokens: list[Token]) -> list[str]:
        python = []
        indent_level = 0

        for token in tokens:
            if token.token_type == TokenType.IF:
                python.append("    " * indent_level + f"if {token.literal}:")
                indent_level += 1

        return python
