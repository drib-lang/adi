from error import errors
from _token import TokenType, Token
from mem import stack, Value, ValueType
from statement import Statement, StatementType


class Evaluator:
    def __init__(self, statements: list[Statement]) -> None:
        self.statements = statements

    def _check_for_errors(self):
        if len(errors) > 0:
            print(errors.pop(0))
            quit()

    def _is_identifier_defined(self, identifier):
        levels = len(stack)
        for level in range(levels, 0, -1):
            for i, var in enumerate(stack[level - 1]):
                if var.name == identifier:
                    return f"stack[{level-1}][{i}].name"
        return False

    def _convert_to_python(self, type_: str, tokens: list[Token]) -> str:
        python = ""
        for token in tokens:
            match token.token_type:
                case TokenType.VAL:
                    python += ""
                case TokenType.IDENTIFIER:
                    if type_ == StatementType.DECLARATION:
                        ident = self._is_identifier_defined(token.literal)
                        if ident:
                            errors.append(
                                f"syntax error: redeclaration of val '{token.literal}'"
                            )
                        else:
                            stack[-1].append(Value(token.literal, ValueType.NIL, None))
                            ident = f"stack[{len(stack)-1}][-1].value"
                    else:
                        ident = self._is_identifier_defined(token.literal)
                        if not ident:
                            errors.append(
                                f"reference error: {token.literal} is not defined"
                            )
                        else:
                            python += ident
                case TokenType.ASSIGN:
                    python += "="
                case TokenType.STRING:
                    python += token.literal
                case TokenType.LBRACE:
                    python += "("
                case TokenType.RBRACE:
                    python += ")"
                case TokenType.SEMICOLON:
                    python += ""
                case TokenType.COMMA:
                    python += ","
        print(python)
        return python

    def evaluate(self):
        self._check_for_errors()
        for stmt in self.statements:
            self._convert_to_python(stmt.type, stmt.tokens)
