from _token import TokenType
from lexer import Lexer

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

while True:
    scanned = input(">> ")

    if scanned in ("exit", "quit"):
        print("Exiting...")
        break

    lexer = Lexer(scanned)
    tok = lexer.next_token()
    print(tok)

    while tok.type != TokenType.TT_EOF:
        tok = lexer.next_token()
        print(tok)
