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


env = {
    "add": lambda a, b: str(int(a) + int(b)),
    "sub": lambda a, b: str(int(a) - int(b)),
    "mul": lambda a, b: str(int(a) * int(b)),
    "div": lambda a, b: str(int(a) // int(b)),
    "pow": lambda a, b: str(int(a) ** int(b)),
    "mod": lambda a, b: str(int(a) % int(b)),
    "gt": lambda a, b: int(a) > int(b),
    "lt": lambda a, b: int(a) < int(b),
    "geq": lambda a, b: int(a) >= int(b),
    "leq": lambda a, b: int(a) <= int(b),
    "eqs": lambda a, b: a == b,
    "not": lambda x: not x,
    "println": lambda x: print(x),
}

if __name__ == "__main__":
    run_repl(Lexer, Parser, env)
