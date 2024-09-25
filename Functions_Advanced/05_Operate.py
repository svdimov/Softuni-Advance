from functools import reduce


def operate(operator, *args):
    def sum_num():
        return reduce(lambda x, y: x + y, args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def divide():
        if ZeroDivisionError:
            return f"We cannot divide by zero"
        return reduce(lambda x, y: x / y, args)

    mapper = {"+": sum_num, "-": subtract, "*": multiply, "/": divide}
    return mapper[operator]()
    # if operator == "+":
    #     return sum_num()
    # elif operator == "-":
    #     return subtract()
    # elif operator == "*":
    #     return multiply()
    # elif operator == "/":
    #     return divide()


print(operate("+", 1, 2, 3))
print(operate("/", 4, 0))
