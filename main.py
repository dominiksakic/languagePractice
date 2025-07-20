import os 
import sys

from report import error , report
from run import run_file, run_repl

def Python(args: list[str]) -> None: 
    if len(args) > 1:
        print("Usage: plox [script]")
        os._exit(64)
    elif len(args) == 1:
        run_file(args[0])
    else:
        run_repl()



if __name__ == "__main__":
    Python(sys.argv[1:])
