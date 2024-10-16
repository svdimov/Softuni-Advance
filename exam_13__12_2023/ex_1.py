from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
number_worms = len(worms)
matches = 0

while worms and holes:
    cur_worm = worms.pop()
    cur_hole = holes.popleft()

    if cur_worm <= 0:
        holes.appendleft(cur_hole)
        continue

    if cur_worm == cur_hole:
        matches += 1

    else:
        cur_worm -= 3
        worms.append(cur_worm)

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")
if worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
elif number_worms == matches:
    print("Every worm found a suitable hole!")
else:
    print("Worms left: none")
if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
