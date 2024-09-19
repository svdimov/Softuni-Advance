
n = int(input())
diagonal = [[int(cow) for cow in input().split()] for row in range(n)] # [::-1] slice revers in right diagonal

# sum_diagonal = 0
# for row in range(n):
#     for cow in range(n):
#         if row == cow:
#             sum_diagonal += diagonal[row][cow]
sum_diagonal = sum(diagonal[i][i] for i in range(n))


print(sum_diagonal)
