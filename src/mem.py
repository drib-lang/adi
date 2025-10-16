from collections.abc import Callable
from builtin import println, size


class Value:
    def __init__(self, name, type_, value: str | bool | Callable | None):
        self.name = name
        self.type = type_
        self.value = value

    def __repr__(self):
        return (
            f'{{"type": "{self.type}", "name": "{self.name}", "value": "{self.value}"}}'
        )

    def __str__(self):
        return (
            f'{{"type": "{self.type}", "name": "{self.name}", "value": "{self.value}"}}'
        )


stack = [
    [
        Value("PI", "string", "3.141592653589793"),
        Value("E", "string", "2.718281828459045"),
        Value("println", "function", println),
        Value("size", "function", size),
    ]
]
