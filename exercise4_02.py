import sys


def is_wrapped_with_quotes(input: str) -> bool:
    '''check if user input is wrapped by ""
    '''
    if len(input) <= 2 or input[0] != "\"" or input[len(input)-1] != "\"":
        print("use \" to quote your input, and your input can't be empty")
        return False
    else:
        return True


def contains_illegal_charater(input: str) -> bool:
    '''check if user input contains illegal charater \n
    if has, print them out and return True, \n
    otherwise, return False
    '''
    legal_chars = "0123456789+-*/"
    result = False
    for c in input.strip("\""):
        if c in legal_chars:
            pass
        else:
            result = True
            print(f"'{c}' is not allowed")
    return result


def is_operator(char: str) -> bool:
    '''check if the charater is an operator
    '''
    operators = ["+", "-", "*", "/"]
    return char in operators


def contains_operator(input: str) -> bool:
    '''check if input contains an operator
    '''
    result = False
    operators = ["+", "-", "*", "/"]
    for o in operators:
        if o in input:
            result = True
    return result


def find_operator(input: str) -> int:
    '''find the first operator appeared in input \n
    return it's index in input
    '''
    operators = ["+", "-", "*", "/"]
    for index, c in enumerate(input):
        if c in operators:
            return index
    return -1


def find_last_operator(input):
    operators = ["+", "-", "*", "/"]
    last_operator_index = -1
    for index, c in enumerate(input):
        if c in operators:
            last_operator_index = index
    return last_operator_index


def occurred_number(input, operator):
    number = 0
    for c in input:
        if c == operator:
            number += 1
    return number


def is_calculable(input):
    result = True
    illegal_opeartors = [
        "++", "+-", "+*", "+/",
        "-+", "--", "-*", "-/",
        "*+", "*-", "**", "*/",
        "/+", "*-", "/*", "//"
    ]
    for io in illegal_opeartors:
        if io in input:
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
            return user_input.strip("\"")
        else:
            continue


def prepare_calculation_args(input, operator_index):
    left_string = input[:operator_index]
    right_string = input[operator_index+1:]
    left_number = None
    right_number = None
    start_index = None
    end_index = None

    previous_operator_index = find_last_operator(left_string)
    if contains_operator(left_string) and previous_operator_index != 0:
        start_index = previous_operator_index+1
        left_number = left_string[previous_operator_index+1:]
    else:
        left_number = left_string
        start_index = 0

    if len(right_string) == 0:
        raise "calculation error: missing right argument"
    if contains_operator(right_string):
        next_operator_index = find_operator(right_string)
        right_number = right_string[:next_operator_index]
        end_index = len(left_string)+len(right_number)
    else:
        right_number = right_string
        end_index = len(input) - 1
    return {
        "left_number": left_number,
        "right_number": right_number,
        "start_index": start_index,
        "end_index": end_index
    }


def process_multiply(input: str):
    calculated_string = input
    while True:
        operator_index = calculated_string.find("*")
        if operator_index == 0:
            print("calculation error: missing left argument for'*'")
            sys.exit()
        if "*" in calculated_string:
            arguments = prepare_calculation_args(
                calculated_string, operator_index)
            result = float(arguments["left_number"]) * \
                float(arguments["right_number"])
            calculated_string = calculated_string[0:arguments["start_index"]] + str(
                result)+calculated_string[arguments["end_index"]+1:]
        else:
            break
    return calculated_string


def process_divide(input):
    calculated_string = input
    while True:
        operator_index = calculated_string.find("/")
        if operator_index == 0:
            print("calculation error: missing left argument for'/'")
            sys.exit()
        if "/" in calculated_string:
            arguments = prepare_calculation_args(
                calculated_string, operator_index)
            result = float(arguments["left_number"]) / \
                float(arguments["right_number"])
            calculated_string = calculated_string[0:arguments["start_index"]] + str(
                result)+calculated_string[arguments["end_index"]+1:]
        else:
            return calculated_string


def process_add(input):
    calculated_string = input
    while True:
        operator_index = calculated_string.find("+")
        if operator_index == 0:
            print("calculation error: missing left argument for'+'")
        if "+" in calculated_string:
            arguments = prepare_calculation_args(
                calculated_string, operator_index)
            result = float(arguments["left_number"]) + \
                float(arguments["right_number"])
            calculated_string = calculated_string[0:arguments["start_index"]] + str(
                result)+calculated_string[arguments["end_index"]+1:]
        else:
            return calculated_string


def process_minus(input):
    calculated_string = input
    while True:
        operator_index = calculated_string.find("-")
        occurred = occurred_number(calculated_string, "-")
        if operator_index == 0 and occurred == 1:
            return calculated_string
        if operator_index == 0 and occurred > 1:
            operator_index = find_operator(calculated_string[operator_index+1:])+1
        if "-" in calculated_string:
            arguments = prepare_calculation_args(
                calculated_string, operator_index)
            result = float(arguments["left_number"]) - \
                float(arguments["right_number"])
            calculated_string = calculated_string[0:arguments["start_index"]] + str(
                result)+calculated_string[arguments["end_index"]+1:]
        else:
            return calculated_string


def calculate():
    input = read_input()
    calculated_string = process_multiply(input)
    calculated_string = process_divide(calculated_string)
    calculated_string = process_add(calculated_string)
    calculated_string = process_minus(calculated_string)
    result = float(calculated_string)
    if result % 1 > 0:
        print(f"Result: {result}")
    else:
        print(f"Result: {int(result)}")


calculate()
