from itertools import permutations
def possible_permutations(numbers_list):
    for perm in permutations(numbers_list):
        yield list(perm)




[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]