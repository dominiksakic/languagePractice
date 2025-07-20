def error(line: int, message: str) -> None:
    report(line, "", messasge)

def report(line: int, whern: str, message: str) -> None:
    print(f"[line {line}] Error {where} : {message}")
