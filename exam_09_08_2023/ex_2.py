n, m = [int(x) for x in input().split()]

matrix = []
boy_pos = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "B":
            boy_pos = [row, col]


directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }
current_pos = boy_pos
while True:
    cmd = input()

    new_row = boy_pos[0] + directions[cmd][0]
    new_col = boy_pos[1] + directions[cmd][1]

    if 4 <= new_row < n and 0 <= new_col < m:
        if matrix[new_row][new_col] == "P":
            matrix[new_row][new_col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")


        elif matrix[new_row][new_col] == "*":
            continue

        elif matrix[new_row][new_col] == "A":
            matrix[new_row][new_col] = "P"
            matrix[current_pos[0]][current_pos[1]] = "B"
            print("Pizza is delivered on time! Next order...")
            break
        else:
            matrix[new_row][new_col] = "."

        boy_pos = [new_row, new_col]
    else:
        matrix[current_pos[0]][current_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

for mat in matrix:
    print(''.join(mat))

# n, m = [int(x) for x in input().split()]
#
# matrix = []
# boy_pos = []
# for row in range(n):
#     matrix.append(list(input()))
#     for col in range(m):
#         if matrix[row][col] == "B":
#             boy_pos = [row, col]
#
# directions = {'up': (-1, 0),
#               'down': (1, 0),
#               'left': (0, -1),
#               'right': (0, 1)
#               }
# current_pos = boy_pos
# while True:
#     cmd = input()
#
#     new_row = boy_pos[0] + directions[cmd][0]
#     new_col = boy_pos[1] + directions[cmd][1]
#
#     if not (0 <= new_row < n and 0 <= new_col < m):
#         print("The delivery is late. Order is canceled.")
#         matrix[current_pos[0]][current_pos[1]] = " "
#         break
#
#     if matrix[new_row][new_col] == "*":
#         continue
#     boy_pos = [new_row, new_col]
#
#     if matrix[new_row][new_col] == "P":
#         matrix[new_row][new_col] = "R"
#         print("Pizza is collected. 10 minutes for delivery.")
#         continue
#     elif matrix[new_row][new_col] == "A":
#         matrix[new_row][new_col] = "P"
#         matrix[current_pos[0]][current_pos[1]] = "B"
#         print("Pizza is delivered on time! Next order...")
#         break
#
#     matrix[new_row][new_col] = "."
#
# for m in matrix:
#     print(''.join(m))
