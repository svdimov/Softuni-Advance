from math import sqrt
def get_primes(numbers_list):

    for num in numbers_list:
        if num < 2:
            continue
        for i in range(2,int(sqrt(num))+1): # or for i in range(2,int(num**0.5)+1)
            if num % i == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print('========================================')
print(list(get_primes([-2, 0, 0, 1, 1, 0])))