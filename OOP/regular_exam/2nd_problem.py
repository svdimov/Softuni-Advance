n, m = [int(x) for x in input().split(', ')]

matrix = []
c_pos = []
time_bomb = 16
bomb_pos = []
first_pos = []

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "C":
            c_pos = [row, col]
            first_pos = [row, col]
        elif matrix[row][col] == "B":
            bomb_pos = [row, col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

bomb_defuse = 0

while True:
    if time_bomb <= 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {bomb_defuse} second/s.")
        break

    cmd = input()
    if cmd in directions:
        new_row = c_pos[0] + directions[cmd][0]
        new_col = c_pos[1] + directions[cmd][1]

        time_bomb -= 1

        if time_bomb < 0:
            print("Terrorists win!")
            print("Bomb was not defused successfully!")
            print(f"Time needed: {bomb_defuse} second/s.")
            break

        if 0 <= new_row < n and 0 <= new_col < m:
            if matrix[new_row][new_col] == "*":

                matrix[c_pos[0]][c_pos[1]] = "*"
                c_pos = [new_row, new_col]
            elif matrix[new_row][new_col] == "B":

                matrix[c_pos[0]][c_pos[1]] = "*"
                c_pos = [new_row, new_col]
            elif matrix[new_row][new_col] == "T":
                matrix[new_row][new_col] = "*"
                print("Terrorists win!")
                break

    elif cmd == "defuse":
        time_bomb -= 2
        if c_pos == bomb_pos:
            time_bomb -= 2
            if time_bomb >= 0:
                matrix[bomb_pos[0]][bomb_pos[1]] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {time_bomb} second/s remaining.")
                break
            else:
                matrix[bomb_pos[0]][bomb_pos[1]] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {time_bomb} second/s.")
                break

if matrix[bomb_pos[0]][bomb_pos[1]] not in ['D', 'X']:
    matrix[bomb_pos[0]][bomb_pos[1]] = 'B'

matrix[first_pos[0]][first_pos[1]] = "C"

for row in matrix:
    print("".join(row))