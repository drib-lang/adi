import sys

sys.path.append("src")

from parser import Parser
from token_ import TokenType, Token


def test_variable_declaration():
    # val my_variable = "hello, world!";
    tokens = [
        Token(TokenType.VAL, "val"),
        Token(TokenType.IDENTIFIER, "my_variable"),
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.STRING, '"hello, world!"'),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.EOF, ""),
    ]
    p = Parser(tokens)
    py_code = p.parse_program()
    assert py_code == 'my_variable = "hello, world!"'


def test_function_declaration():
    # fun my_function(a, b) { return add(a, b); }
    tokens = [
        Token(TokenType.FUNCTION, "fun"),
        Token(TokenType.IDENTIFIER, "my_function"),
        Token(TokenType.LPAREN, "("),
        Token(TokenType.IDENTIFIER, "a"),
        Token(TokenType.COMMA, ","),
        Token(TokenType.IDENTIFIER, "b"),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.LBRACE, "{"),
        Token(TokenType.RETURN, "return"),
        Token(TokenType.IDENTIFIER, "add"),
        Token(TokenType.LPAREN, "("),
        Token(TokenType.IDENTIFIER, "a"),
        Token(TokenType.COMMA, ","),
        Token(TokenType.IDENTIFIER, "b"),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.RBRACE, "}"),
        Token(TokenType.EOF, ""),
    ]
    p = Parser(tokens)
    py_code = p.parse_program()
    expected = "def my_function(a, b):\n" + "    return add(a,b)"
    assert py_code == expected


def test_loop_with_next_and_out():
    # loop { next; out; }
    tokens = [
        Token(TokenType.LOOP, "loop"),
        Token(TokenType.LBRACE, "{"),
        Token(TokenType.NEXT, "next"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.OUT, "out"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.RBRACE, "}"),
        Token(TokenType.EOF, ""),
    ]
    p = Parser(tokens)
    py_code = p.parse_program()
    expected = "while True:\n" + "    continue\n" + "    break"
    assert py_code == expected
