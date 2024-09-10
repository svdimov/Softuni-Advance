from collections import deque

def fill_cups_and_bottles(cups, bottles):

    cups = deque(map(int, cups.split()))
    bottles = deque(map(int, bottles.split()))

    wasted_water = 0

    while cups and bottles:
        current_cup = cups[0]
        current_bottle = bottles.pop()

        if current_bottle >= current_cup:
            wasted_water += (current_bottle - current_cup)
            cups.popleft()
        else:
            cups[0] -= current_bottle


    if cups:
        print("Cups:", " ".join(map(str, cups)))
    else:
        print("Bottles:", " ".join(map(str, bottles)))

    print(f"Wasted litters of water: {wasted_water}")



input_cups = input()
input_bottles = input()
fill_cups_and_bottles(input_cups, input_bottles)
