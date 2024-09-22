presents = int(input())
size = int(input())

matrix = []
santa_position = []
nice_kids = 0
nice_kids_gifted = 0

for rol in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[rol][col] == "S":
            santa_position = [rol, col]
        elif matrix[rol][col] == "V":
            nice_kids += 1
direction = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    r, c = santa_position[0] + direction[command][0], santa_position[1] + direction[command][1]
    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "V":
            presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = '-'
        elif matrix[r][c] == "C":
            for dir_value in direction.values():
                next_r,next_c = r + dir_value[0], c + dir_value[1]
                if matrix[next_r][next_c] in 'VX' and presents > 0:
                    presents-=1
                    if matrix[next_r][next_c] == "V":
                        nice_kids_gifted+=1
                    matrix[next_r][next_c] = "-"
        matrix[santa_position[0]][santa_position[1]] = '-'
        santa_position = [r,c]
        matrix[r][c] = 'S'


if presents < 1 and nice_kids_gifted < nice_kids :
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)

if nice_kids_gifted<nice_kids :
    print(f'No presents for {nice_kids - nice_kids_gifted} nice kid/s.')
else:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
