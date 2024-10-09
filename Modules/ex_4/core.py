
from Modules.ex_4.error import UnknownSignError


def sum_nums(num1, num2):
    pass


def subtract_nums(num1, num2):

    return num1 - num2


def rise_nums(num1, num2):
    return  num1 ** num2


def multiply_nums(num1, num2):

    return num1 * num2


def divide_nums(num1, num2):

    return num1 / num2

mapper = {
    "/": divide_nums,
    "*": multiply_nums,
    "-": subtract_nums,
    "+": sum_nums,
    "^": rise_nums
}
def execute(num1, sign, num2):

    if sign in mapper:
        respective_function = mapper[sign]
        return respective_function(num1,num2)
    raise UnknownSignError("Please provide a valid sign")


