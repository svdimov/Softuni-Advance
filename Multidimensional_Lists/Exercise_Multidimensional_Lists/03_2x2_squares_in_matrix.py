row_num, cow_num = [int(x) for x in input().split()]

matrix = [[cow for cow in input().split()] for row in range(row_num)]
counter = 0
for r in range(row_num - 1):
    for c in range(cow_num - 1):
        ch1 = matrix[r][c]
        ch2 = matrix[r][c+1]
        ch3 = matrix[r+1][c]
        ch4 = matrix[r+1][c+1]
        if ch1 == ch2 == ch3 == ch4:
            counter +=1

print(counter) 