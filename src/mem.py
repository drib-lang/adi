from collections.abc import Callable
from builtin import println, size, five


class ValueType:
    STRING = "STRING"
    FUNCTION = "FUNCTION"
    BOOLEAN = "BOOLEAN"
    NIL = "NIL"


class Value:
    def __init__(self, name, type_, value: str | bool | Callable | None):
        self.name = name
        self.type = type_
        self.value = value

    def __repr__(self):
        return (
            f'{{"type": "{self.type}", "name": "{self.name}", "value": "{self.value}"}}'
        )

    def __str__(self) -> str:
        return self.__repr__()


stack = [
    [
        Value("PI", ValueType.STRING, "3.141592653589793"),
        Value("E", ValueType.STRING, "2.718281828459045"),
        Value("println", ValueType.FUNCTION, println),
        Value("size", ValueType.FUNCTION, size),
        Value("five", ValueType.FUNCTION, five),
    ]
]
