n1, n2 = [int(x) for x in input().split(', ')]

matrix = [[int(row)for row in input().split(', ')]for cow in range(n1)]
# for row in range(n1):
#     data = [int(x) for x in input().split(', ')]
#     matrix.append(data)

sum_matrix = sum(sum(x) for x in matrix)
# for i in matrix:
#     sum_matrix+= sum(i)
print(sum_matrix)
print(matrix)