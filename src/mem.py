from collections.abc import Callable
from builtin import println, size, add, sub, mul, div, mod, pow


class Value:
    def __init__(self, name, value: str | bool | Callable | None):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'{{"name": "{self.name}", "value": "{self.value}"}}'

    def __str__(self) -> str:
        return self.__repr__()


stack = [
    [
        Value("PI", "3.141592653589793"),
        Value("E", "2.718281828459045"),
        Value("println", println),
        Value("size", size),
        Value("add", add),
        Value("sub", sub),
        Value("mul", mul),
        Value("div", div),
        Value("mod", mod),
        Value("pow", pow),
    ]
]
