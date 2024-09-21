n = int(input())

matrix = [[int(j) for j in input().split()] for i in range(n)]

bombs = [[int(b) for b in bomb.split(',')] for bomb in input().split()]


def cells(x, y, s):
    cell = []
    '''
     x = x1 , y1 
    123
    4X5
    678
    '''
    if x - 1 in range(s) and y - 1 in range(s):  # 1
        cell.append((x - 1, y - 1))
    if x - 1 in range(s) and y in range(s):  # 2
        cell.append((x - 1, y))
    if x - 1 in range(s) and y + 1 in range(s):  # 3
        cell.append((x - 1, y + 1))
    if x in range(s) and y - 1 in range(s):  # 4
        cell.append((x, y - 1))
    if x in range(s) and y + 1 in range(s):  # 5
        cell.append((x, y + 1))
    if x + 1 in range(s) and y - 1 in range(s):  # 6
        cell.append((x + 1, y - 1))
    if x + 1 in range(s) and y in range(s):  # 7
        cell.append((x + 1, y))
    if x + 1 in range(s) and y + 1 in range(s):  # 8
        cell.append((x + 1, y + 1))
    return cell


for b in bombs:
    row = b[0]
    col = b[1]
    current_bomb = matrix[row][col]
    if current_bomb > 0:
        near_cells = cells(row, col, n)
        for r, c in near_cells:
            if matrix[r][c] > 0:
                matrix[r][c] -= current_bomb
        matrix[row][col] = 0

result_c = 0
result_sum = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            result_c += 1
            result_sum+= matrix[row][col]

print(f'Alive cells: {result_c}')
print(f'Sum: {result_sum}')
for mat in matrix:
    print(*mat)
