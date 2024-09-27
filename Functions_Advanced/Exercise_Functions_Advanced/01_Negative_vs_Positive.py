def negative_positive(*args):
    negative_sum = sum(x for x in args if x < 0)
    positive_sum = sum(x for x in args if x > 0)
    return negative_sum, positive_sum

 


number = [int(x) for x in input().split()]
n_sum, p_sum = negative_positive(*number)
print(n_sum)
print(p_sum)
if abs(n_sum) > p_sum:

    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
