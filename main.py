import os 
import sys

def Python(args=[]): 
    if(len(args) > 1):
        print("Usage: plox [script]")
        os._exit(64)
    elif (len(args) == 1):
            with open("file", "r") as f:
                print(f"file: {f}")
                print("run function")
    else:
        for line in sys.stdin:
            if line == None:
                break
            print(line)


if __name__ == "__main__":
    Python()
