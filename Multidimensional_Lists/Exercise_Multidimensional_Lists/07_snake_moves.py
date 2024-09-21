rows, cols = [int(x) for x in input().split()]

word = input()
matrix = [['' for _ in range(cols)] for row in range(rows)]
index = 0
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = word[index]
            index = (index+ 1) % len(word)
    else:
        for col in range(cols-1,-1,-1):
            matrix[row][col] = word[index]
            index = (index + 1) % len(word)

for i in matrix:
    print(''.join(i))