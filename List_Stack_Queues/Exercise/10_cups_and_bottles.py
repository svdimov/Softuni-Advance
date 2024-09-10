from collections import deque

cups_ = deque(int(x) for x in input().split())
bottles_ = deque(int(x) for x in input().split())

wasted_water = 0
while cups_ and bottles_:
    current_cup = cups_[0]
    while current_cup > 0:
        current_bottle = bottles_.pop()
        current_cup -= current_bottle
    wasted_water -= current_cup
    cups_.popleft()
if cups_:
    print(f"Cups: {' '.join(map(str,cups_))}")
if bottles_:
    print(f"Bottles: {' '.join(str(x) for x in bottles_)}")
print(f"Wasted litters of water: {wasted_water}")