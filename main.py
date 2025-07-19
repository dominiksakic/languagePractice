import os 
import sys

def Python(args=[]): 
    if len(args) > 1:
        print("Usage: plox [script]")
        os._exit(64)
    elif len(args) == 1:
        try:
            with open(args[0], "r") as f:
                code = f.read()
                print(code)
        except FileNotFoundError:
            print(f"File not found: {args[0]}")
            os._exit(66)
    else:
        for line in sys.stdin:
            print(line, end="")


if __name__ == "__main__":
    Python(sys.argv[1:])
