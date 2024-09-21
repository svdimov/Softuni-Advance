rows, cols = [int(x) for x in input().split()]

matrix = [[j for j in input().split()] for i in range(rows)]
command = ['swap', 'END']
while True:
    user_input = input().split()
    cmd = user_input[0]
    if cmd == "END":
        break
    elif cmd not in command or len(user_input) != 5:
        print('Invalid input!')
        continue
    elif cmd == 'swap':
        row_1, col_1, row_2, col_2 = int(user_input[1]), int(user_input[2]) \
            , int(user_input[3]), int(user_input[4])
        if 0 <= row_1 < rows and 0 <= row_2 < rows and \
                0 <= col_1 < cols and 0 <= col_2 < cols:
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for row in matrix:
                print(*row)

        else:
            print('Invalid input!')
