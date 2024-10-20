n, m = map(int, input().split(", "))
matrix = []
player_pos = None
seconds = 16

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(n):
    line = list(input())
    if "C" in line:
        col = line.index("C")
        player_pos = (row, col)
    matrix.append(line)

matrix[player_pos[0]][player_pos[1]] = "*"
first_pos = player_pos

t_win = False
bomb_exploded = False
time_up = False

while True:
    command = input()

    if command in directions:
        next_row = player_pos[0] + directions[command][0]
        next_col = player_pos[1] + directions[command][1]

        if 0 <= next_row < n and 0 <= next_col < m:
            player_pos = (next_row, next_col)
            element = matrix[next_row][next_col]

            if element == "T":
                t_win = True
                matrix[next_row][next_col] = "*"
                break

        seconds -= 1

    elif command == "defuse":
        if matrix[player_pos[0]][player_pos[1]] == "B":
            seconds -= 4
            if seconds >= 0:
                matrix[player_pos[0]][player_pos[1]] = "D"
                break
            else:
                bomb_exploded = True
                break
        else:
            seconds -= 2

    if not seconds:
        time_up = True
        break

if bomb_exploded:
    matrix[player_pos[0]][player_pos[1]] = "X"
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(seconds)} second/s.")

elif time_up:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(seconds)} second/s.")
elif t_win:
    print("Terrorists win!")

else:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {seconds} second/s remaining.")
    matrix[player_pos[0]][player_pos[1]] = "D"

matrix[first_pos[0]][first_pos[1]] = "C"

for row in matrix:
    print(*row, sep='')