from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        sum_args = reduce(lambda x,y: x+y,args)
        return sum_args

    @staticmethod
    def multiply(*args):
        multiply_args = reduce(lambda x,y:x*y,args)
        return multiply_args

    @staticmethod
    def divide(*args):
        try:
            result = reduce(lambda x,y:x/y,args)
            return result
        except ZeroDivisionError:
            return "Can not divide by zero"

    @staticmethod
    def subtract(*args):
        result = reduce(lambda x,y:x-y,args)
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))



