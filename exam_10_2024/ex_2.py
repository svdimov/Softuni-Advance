n = int(input())

matrix = []
p_health = 100
p_position = []
p_dead = False
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'P':
            p_position = [row, col]

# print(*matrix,sep='\n')
# print(p_position)


directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }

while p_health > 0:
    cmd = input()

    new_row = p_position[0] + directions[cmd][0]
    new_col = p_position[1] + directions[cmd][1]

    matrix[p_position[0]][p_position[1]] = '-'

    if not (0 <= new_row < n and 0 <= new_col < n):
        matrix[p_position[0]][p_position[1]] = 'P'
        continue

    if matrix[new_row][new_col] == 'M':
        p_health -= 40
        if p_health <= 0:
            p_health = 0
            matrix[new_row][new_col] = 'P'
            p_dead = True
            break
        else:
            matrix[new_row][new_col] = '-'

    elif matrix[new_row][new_col] == 'H':
        p_health += 15
        if p_health > 100:
            p_health = 100

        matrix[new_row][new_col] = '-'

    elif matrix[new_row][new_col] == 'X':
        matrix[new_row][new_col] = 'P'
        p_position = [new_row,new_col]
        break
    p_position = [new_row, new_col]

if p_dead:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {p_health} units")
for mat in matrix:
    print(''.join(mat))

