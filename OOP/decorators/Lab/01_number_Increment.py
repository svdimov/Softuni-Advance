def number_increment(numbers):

    def increase():
        res = [el+1 for el in numbers]
        return res

    return increase()


print(number_increment([1, 2, 3]))
