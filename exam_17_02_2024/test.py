n, m = [int(x) for x in input().split(",")]

mat = []
m_pos = []
all_cheese = 0
for r in range(n):
    mat.append(list(input()))
    for c in range(m):
        if mat[r][c] == "M":
            m_pos = [r, c]
        elif mat[r][c] == "C":
            all_cheese += 1

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

last_pos = []
mat[m_pos[0]][m_pos[1]] = "*"  # $ Mark the initial position of the mouse with "*"
current_cheese = 0

while True:
    cmd = input()

    if cmd == "danger":  # $ Correct placement of the danger check
        if current_cheese != all_cheese:
            mat[m_pos[0]][m_pos[1]] = "M"  # $ Mark the mouse's last known position
            print("Mouse will come back later!")
        break

    # Move the mouse according to the command
    new_r = m_pos[0] + directions[cmd][0]  # $ Access full string, not cmd[1]
    new_c = m_pos[1] + directions[cmd][1]

    if 0 <= new_r < n and 0 <= new_c < m:  # $ Check for valid bounds
        if mat[new_r][new_c] == "C":
            current_cheese += 1
            mat[new_r][new_c] = "*"  # $ Cheese eaten, mark with "*"
            m_pos = [new_r, new_c]  # $ Update mouse position
            if current_cheese == all_cheese:
                mat[new_r][new_c] = "M"  # $ Last known position of the mouse
                print("Happy mouse! All the cheese is eaten, good night!")
                break

        elif mat[new_r][new_c] == "T":
            mat[new_r][new_c] = "M"  # $ Mouse is trapped, mark position
            print("Mouse is trapped!")
            break

        elif mat[new_r][new_c] == "@":
            continue  # $ Wall, skip the move

        elif mat[new_r][new_c] == "*":
            m_pos = [new_r, new_c]  # $ Update mouse position when on empty space

    else:  # $ Mouse steps outside the cupboard
        print("No more cheese for tonight!")
        mat[m_pos[0]][m_pos[1]] = "M"  # $ Mark the last position of the mouse
        break

# Print the final state of the matrix
for row in mat:
    print(''.join(row))
