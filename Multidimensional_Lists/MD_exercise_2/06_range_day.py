Size = 5
matrix = []
targets = 0
my_position = []

for row in range(Size):
    matrix.append(input().split())
    for col in range(Size):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

direction = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
targets_down = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'shoot':
        dir_row, dir_col = direction[command[1]]
        row = my_position[0] + dir_row
        col = my_position[1] + dir_col

        while 0 <= row < Size and 0 <= col < Size:
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets -= 1
                targets_down.append([row, col])
                break
            row += dir_row
            col += dir_col
        if targets == 0:
            print(f'Training completed! All {len(targets_down)} targets hit.')
            break

    elif command[0] == 'move':
        dir_row,dir_col = direction[command[1]]
        steps = int(command[2])

        new_row = my_position[0] + dir_row * steps
        new_col = my_position[1] + dir_col  * steps

        if 0 <= new_row < Size and 0 <= new_col < Size and matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [new_row, new_col]
if targets > 0:
    print(f'Training not completed! {targets} targets left.')
[print(r) for r in targets_down]
