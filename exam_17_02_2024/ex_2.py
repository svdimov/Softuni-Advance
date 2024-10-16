n = int(input())

armor = 300
matr = []
j_post = []
enemy_count = 0
for row in range(n):
    matr.append(list(input()))
    for col in range(n):
        if matr[row][col] == "J":
            j_post = [row, col]
        elif matr[row][col] == "E":
            enemy_count += 1

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }

while True:
    cmd = input()
    new_row = j_post[0] + directions[cmd][0]
    new_col = j_post[1] + directions[cmd][1]

    if 0 <= new_row < n and 0 <= new_col < n:
        matr[j_post[0]][j_post[1]] = "-"

        if matr[new_row][new_col] == "E":
            armor -= 100
            enemy_count -= 1

            if enemy_count == 0:
                matr[new_row][new_col] = "J"
                print("Mission accomplished, you neutralized the aerial threat!")
                break

            matr[new_row][new_col] = "-"

        elif matr[new_row][new_col] == "R":
            matr[new_row][new_col] = "-"
            armor = 300

        j_post = [new_row, new_col]
        matr[new_row][new_col] = "J"

    if armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates {j_post}!")
        break
for mat in matr:
    print(''.join(mat))
