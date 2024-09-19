n = int(input())
matrix = [[ch for ch in input() ]for i in range(n)]
symbol_input = input()
result = None
for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol_input:
            result = (i,j)
            print(result)
            exit()

if not result:
    print(f'{symbol_input} does not occur in the matrix')




