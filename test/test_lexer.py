import sys

sys.path.append("src")

from lexer import Lexer


def test_variable_declaration():
    c = """
    val a = "this is a text";
    val b = nil;
    """
    l = Lexer(c)
    toks = l.tokenize()
    expected = [
        {"token_type": "VAL", "literal": "val"},
        {"token_type": "IDENTIFIER", "literal": "a"},
        {"token_type": "ASSIGN", "literal": "="},
        {"token_type": "STRING", "literal": '"this is a text"'},
        {"token_type": ";", "literal": ";"},
        {"token_type": "VAL", "literal": "val"},
        {"token_type": "IDENTIFIER", "literal": "b"},
        {"token_type": "ASSIGN", "literal": "="},
        {"token_type": "NIL", "literal": "nil"},
        {"token_type": ";", "literal": ";"},
        {"token_type": "EOF", "literal": ""},
    ]

    for i, e in enumerate(expected):
        token_type = toks[i].token_type
        token_literal = toks[i].literal

        assert token_type == e["token_type"]
        assert token_literal == e["literal"]


def test_function_declaration():
    c = """
    fun my_print(a) {
        println(a);
    }
    my_print("42");
    """
    l = Lexer(c)
    toks = l.tokenize()
    expected = [
        {"token_type": "FUNCTION", "literal": "fun"},
        {"token_type": "IDENTIFIER", "literal": "my_print"},
        {"token_type": "(", "literal": "("},
        {"token_type": "IDENTIFIER", "literal": "a"},
        {"token_type": ")", "literal": ")"},
        {"token_type": "{", "literal": "{"},
        {"token_type": "IDENTIFIER", "literal": "println"},
        {"token_type": "(", "literal": "("},
        {"token_type": "IDENTIFIER", "literal": "a"},
        {"token_type": ")", "literal": ")"},
        {"token_type": ";", "literal": ";"},
        {"token_type": "}", "literal": "}"},
        {"token_type": "IDENTIFIER", "literal": "my_print"},
        {"token_type": "(", "literal": "("},
        {"token_type": "STRING", "literal": '"42"'},
        {"token_type": ")", "literal": ")"},
        {"token_type": ";", "literal": ";"},
        {"token_type": "EOF", "literal": ""},
    ]

    for i, e in enumerate(expected):
        token_type = toks[i].token_type
        token_literal = toks[i].literal

        assert token_type == e["token_type"]
        assert token_literal == e["literal"]


def test_loop_next_out_tokens():
    c = """
    loop {
        next;
        out;
    }
    """
    l = Lexer(c)
    toks = l.tokenize()
    expected = [
        {"token_type": "LOOP", "literal": "loop"},
        {"token_type": "{", "literal": "{"},
        {"token_type": "NEXT", "literal": "next"},
        {"token_type": ";", "literal": ";"},
        {"token_type": "OUT", "literal": "out"},
        {"token_type": ";", "literal": ";"},
        {"token_type": "}", "literal": "}"},
        {"token_type": "EOF", "literal": ""},
    ]

    for i, e in enumerate(expected):
        token_type = toks[i].token_type
        token_literal = toks[i].literal

        assert token_type == e["token_type"]
        assert token_literal == e["literal"]
