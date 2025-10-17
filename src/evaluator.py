from error import errors
from mem import stack, Value
from _token import TokenType, Token
from statement import Statement, StatementType


class Evaluator:
    def __init__(self, statements: list[Statement]) -> None:
        self.indentation_level = 0
        self.statements = statements

    def _check_for_errors(self):
        if len(errors) > 0:
            print(errors.pop(0))
        errors.clear()

    def _is_identifier_defined(self, identifier):
        levels = len(stack)
        for level in range(levels, 0, -1):
            for i, var in enumerate(stack[level - 1]):
                if var.name == identifier:
                    return f"stack[{level-1}][{i}].value"
        return False

    def _evaluate_declaration(self, tokens: list[Token]) -> str:
        python = []
        tokens.pop(0)  # remove 'val' token
        name = tokens.pop(0).literal  # get identifier name
        if self._is_identifier_defined(name):
            errors.append(f"syntax error: redeclaration of val {name}")
            return ""
        else:
            tokens.pop(0)  # remove '=' token
            python.append(f'stack[{self.indentation_level}].append(Value("{name}",')
            for tok in tokens:
                if tok.token_type in (TokenType.SEMICOLON, TokenType.EOF):
                    break
                if tok.token_type in (
                    TokenType.STRING,
                    TokenType.LPAREN,
                    TokenType.RPAREN,
                    TokenType.LBRACE,  # TODO: remove from here
                    TokenType.RBRACE,  # TODO: remove from here
                    TokenType.COMMA,
                ):
                    python.append(f"{tok.literal}")
                if tok.token_type == TokenType.TRUE:
                    python.append("True")
                if tok.token_type == TokenType.FALSE:
                    python.append("False")
                if tok.token_type == TokenType.NIL:
                    python.append("None")
                if tok.token_type == TokenType.IDENTIFIER:
                    ident = self._is_identifier_defined(tok.literal)
                    if ident:
                        python.append(ident)
                    else:
                        errors.append(f"reference error: {tok.literal} is not defined")
                        return ""
        python.append("))")
        return "".join(python)

    def _evaluate_expression(self, tokens: list[Token]) -> str:
        pass

    def evaluate(self):
        self._check_for_errors()
        for stmt in self.statements:
            if stmt.type == StatementType.DECLARATION:
                python = self._evaluate_declaration(stmt.tokens)
                print(python)
                exec(python)
            if stmt.type == StatementType.EXPRESSION:
                pass
        self._check_for_errors()
        print(stack)
