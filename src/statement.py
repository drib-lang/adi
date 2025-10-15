from _token import Token


class Statement:
    def __init__(self, type_: str, tokens: list[Token]) -> None:
        self.type = type_
        self.tokens = tokens
