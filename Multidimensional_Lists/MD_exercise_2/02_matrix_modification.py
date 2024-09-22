n = int(input())

matrix = [[int(i) for i in input().split()] for x in range(n)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    cmd = command[0]
    row = int(command[1])
    col = int(command[2])
    number = int(command[3])

    if row < 0 or row >= n or col < 0 or col >= n:
        print('Invalid coordinates')
        continue
    if cmd == "Add":
        matrix[row][col]+= number

    elif cmd == "Subtract":
        matrix[row][col]-=number

for mat in matrix:
    print(*mat)
