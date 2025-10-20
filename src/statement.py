from token_ import Token


class Statement:
    def __init__(self, type_: str, tokens: list[Token]) -> None:
        self.type = type_
        self.tokens = tokens

    def __repr__(self):
        return f'{{"type": "{self.type}", "tokens": {self.tokens}}}'

    def __str__(self) -> str:
        return self.__repr__()


class StatementType:
    DECLARATION = "DECLARATION"
    EXPRESSION = "EXPRESSION"
    BLOCK = "BLOCK"
    WHEN = "WHEN"
    LOOP = "LOOP"
    FUNCTION = "FUNCTION"
    RETURN = "RETURN"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
