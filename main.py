import os 
import sys

def Python(args: list[str]) -> None: 
    if len(args) > 1:
        print("Usage: plox [script]")
        os._exit(64)
    elif len(args) == 1:
        run_file(args[0])
    else:
        run_repl()

def run_file(path: str) -> None:
    try:
        with open(path, "r") as f:
            code = f.read()
            run(code) 
    except FileNotFoundError:
        print(f"File not found: {args[0]}")
        os._exit(66)

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
    for token in source:
        print(token)

def error(line: int, message: str) -> None:
    report(line, "", messasge)

def report(line: int, whern: str, message: str) -> None:
    print(f"[line {line}] Error {where} : {message}")

if __name__ == "__main__":
    Python(sys.argv[1:])
