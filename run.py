import sys
from scanner import scanner

def run_file(path: str) -> None:
    try:
        with open(path, "r") as f:
            code = f.read()
            run(code) 
    except FileNotFoundError:
        print(f"File not found: {args[0]}")
        sys.exit(66)

def run_repl() -> None:
    while True:
        try:
            print("> ", end="", flush=True)
            line: str = sys.stdin.readline().strip()
            if not line:
                break # EOF (Ctrl + D)
            if line == "exit":
                print("Exiting REPL")
                sys.exit(0)
            else:
                run(line)
        except KeyboardInterrupt:
            print("\nExiting on Keyboard interuppt")
            sys.exit(0)

def run(source: str) -> None:
    tokens = scanner(source)
    for token in tokens:
        print(token)
