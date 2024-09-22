n = int(input())

matrix = []
K = []

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            K.append([row, col])
removed_K = 0
position_K = ((1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1))
while True:
    max_hits = 0
    max_K = [0,0]

    for k_row, k_col in K:
        hits = 0
        for move in position_K:
            next_row = k_row + move[0]
            next_col = k_col + move[1]
            if 0 <= next_row < n and 0 <= next_col < n:
                if matrix[next_row][next_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_K = [k_row, k_col]

    if max_hits == 0:
        break
    K.remove(max_K)
    matrix[max_K[0]][max_K[1]] = '0'
    removed_K += 1
print(removed_K)