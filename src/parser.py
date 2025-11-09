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
                self.next_token()
                lines.append(self.parse_val_statement())
            elif tok.token_type == TokenType.FUNCTION:
                lines.append(self.parse_function())
            elif tok.token_type == TokenType.WHEN:
                lines.append(self.parse_when_statement())
            elif tok.token_type == TokenType.LOOP:
                lines.append(self.parse_loop_statement())
            elif tok.token_type == TokenType.NEXT:
                lines.append(self.parse_next_statement())
            elif tok.token_type == TokenType.OUT:
                lines.append(self.parse_out_statement())
            else:
                lines.append(self.parse_expression_statement())
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

        def map_literal(tok):
            if tok == "nil":
                return "None"
            if tok == "true":
                return "True"
            if tok == "false":
                return "False"
            return tok

        rhs = "".join([map_literal(tok) for tok in value_tokens])
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
            elif tok.token_type == TokenType.WHEN:
                body_lines.append(self.parse_when_statement())
            elif tok.token_type == TokenType.VAL:
                body_lines.append(self.parse_val_statement())
            elif tok.token_type == TokenType.LOOP:
                body_lines.append(self.parse_loop_statement())
            elif tok.token_type == TokenType.NEXT:
                body_lines.append(self.parse_next_statement())
            elif tok.token_type == TokenType.OUT:
                body_lines.append(self.parse_out_statement())
            else:
                body_lines.append(self.parse_expression_statement())

        self.indent_level -= 1
        self.next_token()

        return "\n".join([header] + body_lines)

    def parse_return_statement(self):
        self.next_token()  # skip 'return'
        tokens = []
        while self.current_token().token_type not in (
            TokenType.SEMICOLON,
            TokenType.EOF,
        ):
            tokens.append(self.current_token().literal)
            self.next_token()
        if self.current_token().token_type == TokenType.SEMICOLON:
            self.next_token()
        indent = "    " * self.indent_level

        def map_literal(tok):
            if tok == "nil":
                return "None"
            if tok == "true":
                return "True"
            if tok == "false":
                return "False"
            return tok

        return f"{indent}return {''.join([map_literal(tok) for tok in tokens])}"

    def parse_expression_statement(self):
        tokens = []
        while self.current_token().token_type not in (
            TokenType.SEMICOLON,
            TokenType.EOF,
        ):
            tokens.append(self.current_token().literal)
            self.next_token()
        if self.current_token().token_type == TokenType.SEMICOLON:
            self.next_token()
        indent = "    " * self.indent_level

        def map_literal(tok):
            if tok == "nil":
                return "None"
            if tok == "true":
                return "True"
            if tok == "false":
                return "False"
            return tok

        return f"{indent}{''.join([map_literal(tok) for tok in tokens])}"

    def parse_when_statement(self):
        self.next_token()  # skip 'when'
        if self.current_token().token_type != TokenType.LPAREN:
            raise Exception("Syntax error: expected '(' after 'when'")
        self.next_token()  # skip '('
        condition_tokens = []
        paren_count = 1
        while paren_count > 0 and self.current_token().token_type != TokenType.EOF:
            if self.current_token().token_type == TokenType.LPAREN:
                paren_count += 1
            elif self.current_token().token_type == TokenType.RPAREN:
                paren_count -= 1
                if paren_count == 0:
                    break
            condition_tokens.append(self.current_token().literal)
            self.next_token()
        if paren_count != 0:
            raise Exception("Syntax error: missing ')' in when condition")
        condition = "".join(condition_tokens)
        self.next_token()  # skip ')'
        if self.current_token().token_type != TokenType.LBRACE:
            raise Exception("Syntax error: expected '{' after when condition")
        self.next_token()  # skip '{'

        indent = "    " * self.indent_level
        header = f"{indent}if {condition}:"
        self.indent_level += 1

        body_lines = []
        while self.current_token().token_type != TokenType.RBRACE:
            tok = self.current_token()
            if tok.token_type == TokenType.WHEN:
                body_lines.append(self.parse_when_statement())
            elif tok.token_type == TokenType.VAL:
                body_lines.append(self.parse_val_statement())
            elif tok.token_type == TokenType.RETURN:
                body_lines.append(self.parse_return_statement())
            elif tok.token_type == TokenType.LOOP:
                body_lines.append(self.parse_loop_statement())
            elif tok.token_type == TokenType.NEXT:
                body_lines.append(self.parse_next_statement())
            elif tok.token_type == TokenType.OUT:
                body_lines.append(self.parse_out_statement())
            else:
                expr = self.parse_expression_statement()
                body_lines.append(expr)

        self.indent_level -= 1
        self.next_token()

        else_lines = []
        if self.current_token().token_type == TokenType.OTHERWISE:
            self.next_token()  # skip 'otherwise'
            self._expect(TokenType.LBRACE)  # expect '{'
            indent_else = "    " * self.indent_level
            else_lines.append(f"{indent_else}else:")
            self.indent_level += 1
            # now inside else block
            while self.current_token().token_type != TokenType.RBRACE:
                tok = self.current_token()
                if tok.token_type == TokenType.WHEN:
                    else_lines.append(self.parse_when_statement())
                elif tok.token_type == TokenType.VAL:
                    else_lines.append(self.parse_val_statement())
                elif tok.token_type == TokenType.RETURN:
                    else_lines.append(self.parse_return_statement())
                elif tok.token_type == TokenType.LOOP:
                    else_lines.append(self.parse_loop_statement())
                elif tok.token_type == TokenType.NEXT:
                    else_lines.append(self.parse_next_statement())
                elif tok.token_type == TokenType.OUT:
                    else_lines.append(self.parse_out_statement())
                else:
                    expr = self.parse_expression_statement()
                    else_lines.append(expr)
            self.indent_level -= 1
            self.next_token()  # skip '}'

        return "\n".join([header] + body_lines + else_lines)

    def parse_loop_statement(self):
        # current token is 'loop'
        self.next_token()  # move to '{'
        if self.current_token().token_type != TokenType.LBRACE:
            raise Exception("Syntax error: expected '{' after 'loop'")
        self.next_token()  # skip '{'

        indent = "    " * self.indent_level
        header = f"{indent}while True:"
        self.indent_level += 1

        body_lines = []
        while self.current_token().token_type != TokenType.RBRACE:
            tok = self.current_token()
            if tok.token_type == TokenType.WHEN:
                body_lines.append(self.parse_when_statement())
            elif tok.token_type == TokenType.VAL:
                body_lines.append(self.parse_val_statement())
            elif tok.token_type == TokenType.RETURN:
                body_lines.append(self.parse_return_statement())
            elif tok.token_type == TokenType.LOOP:
                body_lines.append(self.parse_loop_statement())
            elif tok.token_type == TokenType.NEXT:
                body_lines.append(self.parse_next_statement())
            elif tok.token_type == TokenType.OUT:
                body_lines.append(self.parse_out_statement())
            else:
                body_lines.append(self.parse_expression_statement())

        self.indent_level -= 1
        self.next_token()  # skip '}'

        return "\n".join([header] + body_lines)

    def parse_next_statement(self):
        # 'next;' -> 'continue'
        self.next_token()  # move past 'next'
        if self.current_token().token_type == TokenType.SEMICOLON:
            self.next_token()
        indent = "    " * self.indent_level
        return f"{indent}continue"

    def parse_out_statement(self):
        # 'out;' -> 'break'
        self.next_token()  # move past 'out'
        if self.current_token().token_type == TokenType.SEMICOLON:
            self.next_token()
        indent = "    " * self.indent_level
        return f"{indent}break"
