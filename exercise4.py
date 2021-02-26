
def interpret_request(request):
    operators_symbols = ["+", "-", "*", "/"]
    operators = []
    for index, symbol in enumerate(request):
        if symbol in operators_symbols:
            operators.append({"index": index, "symbol": symbol})
    elements = []
    start = -1
    for index, operator in enumerate(operators):
        elements.append(request[start+1:operator["index"]])
        elements.append(operator["symbol"])
        start = operator["index"]
        if index == len(operators) - 1:
            elements.append(request[operator["index"]+1:])
    return elements


def calculate_string():
    print("use \"\" to quote your request ")
    request = input("Enter your request: ").strip("\"")
    elements = interpret_request(request)
    print(elements)
    while "+" in elements or "-" in elements or "*" in elements or "/" in elements:
        for index, element in enumerate(elements):
            result = None
            if element == "*":
                result = int(elements[index-1])*int(elements[index+1])
            elif element == "/":
                result = int(elements[index-1])/int(elements[index+1])
            if result is not None:
                elements[index] = result
                elements[index-1] = None
                elements[index+1] = None
                elements = list(filter(lambda e: e is not None, elements))
                print(elements)
                break
            continue
        for index, element in enumerate(elements):
            result = None
            if element == "+":
                result = int(elements[index-1])+int(elements[index+1])
            elif element == "-":
                result = int(elements[index-1])-int(elements[index+1])
            if result != None:
                elements[index] = result
                elements[index-1] = None
                elements[index+1] = None
                elements = list(filter(lambda e: e is not None, elements))
                print(elements)
                break
    print(f"result: {elements[0]}")


calculate_string()
