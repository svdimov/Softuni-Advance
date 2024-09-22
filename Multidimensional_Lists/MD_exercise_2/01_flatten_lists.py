user_input = input().split('|')

matrix = []

for i in range(len(user_input)-1,-1,-1):
    rev = user_input[i].split()
    if rev:
        matrix.append(rev)

for mat in matrix:
    print(*mat,end=' ')