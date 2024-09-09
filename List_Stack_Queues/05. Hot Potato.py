from collections import deque
def hot_potato(kids,n):
    while len(kids) > 1:
        kids.rotate(-(n - 1))
        print(f"Removed {kids.popleft()}")
    print(f"Last is {kids.popleft()}")

kids = deque(input().split())
n = int(input())
hot_potato(kids,n)

