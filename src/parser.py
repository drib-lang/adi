from token_ import Token
from token_ import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.indent_level = 0

    def current_token(self) -> Token:
        return self.tokens[self.position]

    def next_token(self) -> Token:
        self.position += 1
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return Token(TokenType.EOF, "")

    def peek_token(self) -> Token:
        if self.position + 1 < len(self.tokens):
            return self.tokens[self.position + 1]
        return Token(TokenType.EOF, "")

    def _expect(self, token_type: str) -> Token:
        tok = self.current_token()
        if tok.token_type != token_type:
            raise Exception(
                f"Expected token {token_type}, got {tok.token_type} ({tok.literal})"
            )
        self.next_token()
        return tok

    def parse_program(self):
        lines = []
        while self.current_token().token_type != TokenType.EOF:
            tok = self.current_token()

            if tok.token_type == TokenType.VAL:
                lines.append(self.parse_val_statement())
            elif tok.token_type == TokenType.FUNCTION:
                lines.append(self.parse_function())
            elif tok.literal == "if":
                lines.append(self.parse_if_statement())
            else:
                self.next_token()
        return "\n".join(lines)

    def parse_val_statement(self):
        # 'val' already consumed
        name = self._expect(TokenType.IDENTIFIER).literal
        self._expect(TokenType.ASSIGN)

        value_tokens = []
        while self.current_token().token_type not in (
            TokenType.SEMICOLON,
            TokenType.EOF,
        ):
            value_tokens.append(self.current_token().literal)
            self.next_token()

        if self.current_token().token_type == TokenType.SEMICOLON:
            self.next_token()

        rhs = "".join(value_tokens)
        return f"{name} = {rhs}"

    def parse_function(self):
        self.next_token()
        name = self.current_token().literal
        self.next_token()
        self.next_token()

        params = []
        while self.current_token().token_type != TokenType.RPAREN:
            if self.current_token().token_type == TokenType.IDENTIFIER:
                params.append(self.current_token().literal)
            self.next_token()
        self.next_token()
        self.next_token()

        indent = "    " * self.indent_level
        header = f"{indent}def {name}({', '.join(params)}):"
        self.indent_level += 1

        body_lines = []
        while self.current_token().token_type != TokenType.RBRACE:
            tok = self.current_token()
            if tok.token_type == TokenType.RETURN:
                body_lines.append(self.parse_return_statement())
            elif tok.literal == "if":
                body_lines.append(self.parse_if_statement())
            elif tok.token_type == TokenType.VAL:
                body_lines.append(self.parse_val_statement())
            else:
                self.next_token()

        self.indent_level -= 1
        self.next_token()

        return "\n".join([header] + body_lines)

    def parse_return_statement(self):
        self.next_token()
        expr = self.current_token().literal
        self.next_token()
        if self.current_token().token_type == TokenType.SEMICOLON:
            self.next_token()
        indent = "    " * self.indent_level
        return f"{indent}return {expr}"

    def parse_if_statement(self):
        self.next_token()
        self.next_token()
        condition_tokens = []
        while self.current_token().token_type != TokenType.RPAREN:
            condition_tokens.append(self.current_token().literal)
            self.next_token()
        condition = "".join(condition_tokens)
        self.next_token()
        self.next_token()

        indent = "    " * self.indent_level
        header = f"{indent}if {condition}:"
        self.indent_level += 1

        body_lines = []
        while self.current_token().token_type != TokenType.RBRACE:
            tok = self.current_token()
            if tok.literal == "if":
                body_lines.append(self.parse_if_statement())
            elif tok.token_type == TokenType.VAL:
                body_lines.append(self.parse_val_statement())
            elif tok.token_type == TokenType.RETURN:
                body_lines.append(self.parse_return_statement())
            else:
                indent_inner = "    " * self.indent_level
                body_lines.append(f"{indent_inner}{tok.literal}")
                self.next_token()

        self.indent_level -= 1
        self.next_token()

        else_lines = []
        if self.current_token().literal == "otherwise":
            self.next_token()
            self.next_token()
            self.indent_level += 1
            else_lines.append("    " * (self.indent_level - 1) + "else:")
            while self.current_token().token_type != TokenType.RBRACE:
                tok = self.current_token()
                if tok.literal == "if":
                    else_lines.append(self.parse_if_statement())
                else:
                    indent_inner = "    " * self.indent_level
                    else_lines.append(f"{indent_inner}{tok.literal}")
                    self.next_token()
            self.indent_level -= 1
            self.next_token()

        return "\n".join([header] + body_lines + else_lines)
