from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0
while chocolate and milk and milkshakes < 5:
    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolate[-1] == milk[0]:
        milkshakes += 1
        chocolate.pop()
        milk.popleft()

    else:
        milk.rotate(-1)
        chocolate[-1] -= 5
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolate) if chocolate else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk) if milk else 'empty'}")
