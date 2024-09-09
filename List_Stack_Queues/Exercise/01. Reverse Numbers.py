from collections import deque


rev_number = deque(input().split())
new_list = []

for i in rev_number:

    new_list.append(int(i))
print(*new_list[::-1])
