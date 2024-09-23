size = int(input())

directions_inpt = input().split()
matrix =[]
miner_position = []
total_coal = 0


for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "s":
            miner_position = [row,col]
        elif matrix[row][col] == 'c':
            total_coal+=1

collected_coal = 0
direction = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for command in directions_inpt:
    new_row = miner_position[0] + direction[command][0]
    new_col  = miner_position[1] + direction[command][1]

    if 0 <= new_row < size and 0 <= new_col < size:

        miner_position = [new_row,new_col]

        if matrix[new_row][new_col] == 'c':
            collected_coal+=1
            matrix[new_row][new_col]  = '*'
            if collected_coal == total_coal:
                print(f"You collected all coal! ({new_row}, {new_col})")
                break

        if  matrix[new_row][new_col] == 'e':
            print(f"Game over! ({new_row}, {new_col})")
            break
else:
    remaining_coal = total_coal - collected_coal
    print(f"{remaining_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")













