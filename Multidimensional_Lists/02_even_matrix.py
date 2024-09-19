matrix_even = [[int(ev) for ev in input().split(',') if int(ev) % 2 == 0] for row in range(int(input()))]
print(matrix_even)
