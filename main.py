import os 
import sys

def Python(args=[]): 
    if len(args) > 1:
        print("Usage: plox [script]")
        os._exit(64)
    elif len(args) == 1:
        run_file(argv[0])
    else:
        run_repl()

def run_file(path):
    try:
        with open(path, "r") as f:
            code = f.read()
            run(code) 
    except FileNotFoundError:
        print(f"File not found: {args[0]}")
        os._exit(66)

def run_repl():
    while True:
        try:
            print("> ", end="", flush=True)
            line = sys.stdin.readline().strip()
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

def run(source):
    for token in source:
        print(token)

def error(line, message):
    report(line, "", mesesge)

def report(line, where, message):
    print(f"[line {line}] Error {where} : {message}")

if __name__ == "__main__":
    Python(sys.argv[1:])
