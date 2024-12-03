n = int(input())
command = input().split(", ")
mat = []
all_h = 0
s_pos = []
for r in range(n):
    mat.append(list(input()))
    for c in range(n):
        if mat[r][c] == "s":
            s_pos = [r, c]
        elif mat[r][c] == "h":
            all_h += 1

mat[s_pos[0]][s_pos[1]] = "*"
hazelnuts = 0
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for cmd in command:
    if cmd in directions:
        n_row = s_pos[0] + directions[cmd][0]
        n_col = s_pos[1] + directions[cmd][1]
        s_pos = [n_row, n_col]
        if 0 <= n_row < n and 0 <= n_col < n:
            if mat[n_row][n_col] == "h":
                hazelnuts += 1
                mat[n_row][n_col] = "*"
                s_pos = [n_row, n_col]
                if all_h == hazelnuts:
                    print("Good job! You have collected all hazelnuts!")
                    break

            elif mat[n_row][n_col] == "*":
                continue

            elif mat[n_row][n_col] == "t":
                s_pos = [n_row, n_col]
                print("Unfortunately, the squirrel stepped on a trap...")
                break


        else:
            print("The squirrel is out of the field.")
            break


else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
