from lexer import Lexer
from parser import Parser
from _token import TokenType
from evaluator import Evaluator

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
print("(type 'exit' or 'quit' to leave)")

while True:
    scanned = input(">>> ").strip()

    if scanned in ("exit", "quit"):
        break

    lexer = Lexer(scanned)
    tokens = []

    while True:
        tok = lexer.next_token()
        tokens.append(tok)
        if tok.token_type == TokenType.EOF:
            break

    parser = Parser(tokens)
    statements = parser.parse_program()

    evaluator = Evaluator(statements)
    evaluator.evaluate()
