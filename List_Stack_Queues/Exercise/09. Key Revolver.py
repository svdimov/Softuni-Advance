from collections import deque

price_bullet = int(input())
size_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
value = int(input())

counter_bullets = 0
counter = 0

while bullets and locks:

    cur_bullet = bullets.pop()
    cur_lock = locks[0]
    counter_bullets += 1
    counter += 1

    if cur_bullet <= cur_lock:
        locks.popleft()
        print("Bang!")

    else:
        print("Ping!")

    if counter % size_barrel == 0 and bullets:
        print("Reloading!")

money_left = value - (counter_bullets * price_bullet)
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_left}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
