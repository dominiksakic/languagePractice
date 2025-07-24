def error(line: int, message: str) -> None:
    report(line, "", message)

def report(line: int, where: str, message: str) -> None:
    has_error = True
    print(f"[line {line}] Error {where} : {message}")
    return has_error
