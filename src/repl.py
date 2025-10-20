from lexer import Lexer
from token_ import TokenType

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
