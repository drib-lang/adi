from lexer import Lexer
from parser import Parser

print("⢀⢀⢀⢀⢀⢀⢀⢀ D R I B ⢀⢀⢀⢀⢀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⡶⡶⡶⡶⡶⣤⡀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢠⡿⢋⢀⣴⡶⢶⣄⡈⢻⣦⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣠⣴⢿⢁⢀⢸⡷⣶⡶⣻⢀⢀⣹⡄⢀")
print("⢀⢀⢀⢀⢀⢀⢀⣠⣶⡟⡉⢀⢀⢀⢀⡈⢻⡶⢾⢋⣴⣛⣉⣛⣷")
print("⢀⢀⢀⢀⢀⢀⣼⡟⢀⢀⢀⢀⢀⢀⢰⡄⢀⢀⢀⢸⢿⢽⣿⢋⢀")
print("⢀⢀⢀⢀⢠⣿⣡⣴⡖⢀⣀⢀⢀⢀⣼⢇⢀⢀⢀⢀⢀⢀⣿⢀⢀")
print("⢀⢀⢀⢠⡿⢋⣉⣠⡶⡟⢃⢀⣤⡾⢋⢀⢀⢀⢀⢀⢀⢀⣿⢀⢀")
print("⢀⢀⢀⣻⡿⢿⢿⡷⡶⡶⡟⢋⡉⢀⢀⢀⢀⢀⢀⢀⢀⣼⢃⢀⢀")
print("⣀⣴⢟⡋⣠⡴⡟⡷⣤⣀⢀⢀⢀⢀⢀⢀⢀⢀⣠⣴⡞⢁⢀⢀⢀")
print("⢻⢾⣯⢾⢋⢀⢀⢀⡈⡙⢻⡶⡶⡶⡶⢶⡞⡛⢋⢁⢀⢀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⡶⡶⢿⡶⢆⡰⡶⢿⡶⡶⢄⢀⢀⢀⢀⢀")
print("⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀")


def run_repl(lexer_cls, parser_cls, env):
    print("Welcome to Drib! Type 'exit' or 'quit' to quit.")

    buffer = ""
    open_braces = 0

    while True:
        prompt = ">>> " if open_braces == 0 else "... "
        line = input(prompt)

        if line.strip() == "exit" or line.strip() == "quit":
            break

        open_braces += line.count("{")
        open_braces -= line.count("}")

        buffer += line + "\n"

        if open_braces == 0 and buffer.strip():
            try:
                lexer = lexer_cls(buffer)
                tokens = lexer.tokenize()
                parser = parser_cls(tokens)
                python_code = parser.parse_program()
                exec(python_code, env, env)

            except Exception as e:
                print("Error:", e)

            buffer = ""


from builtins_ import env

if __name__ == "__main__":
    run_repl(Lexer, Parser, env)
