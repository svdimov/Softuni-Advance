matrix = [[int(cow) for cow in input().split(',')] for row in range(int(input()))]
flatt_matrix = [j for i in matrix for j in i]

print(flatt_matrix)