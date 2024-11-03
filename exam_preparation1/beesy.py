n = int(input())

matrix = []
bee_position = []
hive_position = []
energy = 15
nectar = 0
restored = False


for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "B":
            bee_position = [row, col]
        elif matrix[row][col] == "H":
            hive_position = [row, col]


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while energy > 0:
    command = input()

    new_row = bee_position[0] + directions[command][0]
    new_col = bee_position[1] + directions[command][1]
    #oposite direction in matrix
    new_row = (new_row + n) % n
    new_col = (new_col + n) % n

    # if new_row < 0:
    #     new_row = n - 1
    # elif new_row >= n:
    #     new_row = 0
    # if new_col < 0:
    #     new_col = n - 1
    # elif new_col >= n:
    #     new_col = 0

    energy -= 1
    matrix[bee_position[0]][bee_position[1]] = "-"
    bee_position = [new_row, new_col]
    current_cell = matrix[new_row][new_col]

    if matrix[new_row][new_col].isdigit():
        nectar+= int(current_cell)
        matrix[new_row][new_col] = '-'

    elif matrix[new_row][new_col] == "H":
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        matrix[new_row][new_col] = 'B'
        break

    if energy <= 0:
        if nectar >= 30 and  not restored:
            additional_energy = nectar - 30
            energy = additional_energy
            nectar = 30
            restored = True

        else:
            print("This is the end! Beesy ran out of energy.")
            matrix[new_row][new_col] = 'B'
            break
    matrix[new_row][new_col] = 'B'


for mat in matrix:
    print(''.join(mat))