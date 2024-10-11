n = int(input())

matrix = []
player_pos = []

stars_count = 2
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            player_pos = [row, col]

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)}

while 0 < stars_count < 10:

    command = input()

    new_row = player_pos[0] + directions[command][0]
    new_col = player_pos[1] + directions[command][1]

    if  not (0 <= new_row < n and 0 <= new_col < n):
        new_row = 0
        new_col = 0


    matrix[player_pos[0]][player_pos[1]] = "."

    if matrix[new_row][new_col] == "*":
        stars_count += 1
        matrix[new_row][new_col] = "."

    elif matrix[new_row][new_col] == "#":
        stars_count -= 1
        new_row, new_col = player_pos
        continue

    player_pos = [new_row, new_col]

if stars_count == 10:
    print(f"You won! You have collected {stars_count} stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_pos[0]}, {player_pos[1]}]")
matrix[player_pos[0]][player_pos[1]] = "P"
for row in matrix:
    print(' '.join(row))
