from collections import deque


def fast_food(food_for_day,orders):

    print(max(orders))

    while orders and food_for_day  >= orders[0]:
        food_for_day -= orders.popleft()

    if orders:
        print(f"Orders left: {' '.join(map(str, orders))}")
    else:
        print('Orders complete')


food_for_day = int(input())
orders = deque(map(int, input().split()))
fast_food(food_for_day,orders)
