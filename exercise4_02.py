def is_wrapped_with_quotes(string):
    if len(string) <= 2 or string[0] != "\"" or string[len(string)-1] != "\"":
        print("use \" to quote your input, and your input can't be empty")
        return False
    else:
        return True


def contains_illegal_charater(string):
    legal_chars = "0123456789+-*/"
    result = False
    for c in string.strip("\""):
        if c in legal_chars:
            pass
        else:
            result = True
            print(f"'{c}' is not allowed")
    return result


def is_calculable(string):
    result = True
    illegal_opeartors = [
        "++", "+-", "+*", "+/",
        "-+", "--", "-*", "-/",
        "*+", "*-", "**", "*/",
        "/+", "*-", "/*", "//"
    ]
    for io in illegal_opeartors:
        if io in string:
            result = False
            print(f"'{io}' is not a legal operator")
        else:
            pass
    return result


def read_input():
    while True:
        user_input = input(
            "Enter your arithmetic: ")
        if is_wrapped_with_quotes(user_input) and not contains_illegal_charater(user_input) and is_calculable(user_input):
            return user_input
        else:
            continue


read_input()
