from django.utils.http import escape_leading_slashes

n1,n2 = [int(x) for x in input().split(', ')]

matrix = [[int(cow) for cow in input().split(', ')]for row in range(n1)]
sum_element = 0
max_sum = float("-inf")
mini_matrix = None
for row in range(n1-1):
    for cow in range(n2-1):
        element = matrix[row][cow]
        next_element = matrix[row][cow+1]
        element_below = matrix[row+1][cow]
        element_diagonal = matrix[row+1][cow+1]

        sum_element = element + next_element + element_below + element_diagonal
        if sum_element > max_sum:
            max_sum = sum_element
            mini_matrix = [[element,next_element],[element_below,element_diagonal]]

print(*mini_matrix[0])
print(*mini_matrix[1])
print(max_sum)