row_num, col_num = [int(x) for x in input().split()]

matrix = [[int(col) for col in input().split()] for row in range(row_num)]
result = float('-inf')

max_row = 0
max_col = 0
for row in range(row_num - 2):
    for col in range(col_num-2):
        sum_mat = 0
        for i in range(row, row+3):
            for j in range(col,col+3):
                sum_mat += matrix[i][j]
        if sum_mat > result:
            result = sum_mat
            max_col = col
            max_row  = row
print(f"Sum = {result}")
for row in range(max_row,max_row+3):
    for col in range(max_col,max_col+3):
        print(matrix[row][col], end=' ')
    print()


