from collections import deque

money = [int(x) for x in input().split()]
price_food = deque(int(x) for x in input().split())
count_food = 0
while money and price_food:
    current_money = money.pop()
    current_price = price_food.popleft()
    if current_money == current_price:
        count_food += 1
    elif current_money > current_price:
        count_food += 1
        current_money -= current_price
        if len(money) == 0:
            money.append(current_money)
        else:
            money[-1] += current_money

if count_food >= 4:
    print(f"Gluttony of the day! Henry ate {count_food} foods.")
else:
    if 2 <= count_food <= 3:
        print(f"Henry ate: {count_food} foods.")
    elif 0 < count_food < 2:
        print(f"Henry ate: {count_food} food.")
    else:
        print(f"Henry remained hungry. He will try next weekend again.")
