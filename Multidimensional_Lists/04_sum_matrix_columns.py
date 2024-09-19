

first_, second_ = [int(x) for x in input().split(', ')]

matrix = [[int(j) for j in input().split()] for i in range(first_)]
#
# for j in range(second_):
#     sum_matrix_cow = 0
#     for i in range(first_):
#         sum_matrix_cow += matrix[i][j]
#     print(sum_matrix_cow)

sum_matrix_cow = [[matrix[i][j] for i in range(first_)]for j in range(second_)]
print(*[sum(x) for x in sum_matrix_cow],sep='\n')