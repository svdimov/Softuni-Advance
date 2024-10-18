n = int(input())

area = []
ship_pos = []
fish = 0
for r in range(n):
    area.append(list(input()))
    for c in range(n):
        if area[r][c] == "S":
            ship_pos = [r, c]

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)}
ship_is_sink = False
while True:
    cmd = input()
    if cmd == "collect the nets":
        break

    new_r = ship_pos[0] + directions[cmd][0]
    new_c = ship_pos[1] + directions[cmd][1]
    #  aко е езивън рейндж продлъжи отдругата страна
    new_r = (new_r + n) % n
    new_c = (new_c + n) % n
    # if new_r < 0:
    #     new_r = n - 1
    # elif new_r >= n:
    #     new_r = 0
    # if new_c < 0:
    #     new_c = n - 1
    # elif new_c >= n:
    #     new_c = 0

    area[ship_pos[0]][ship_pos[1]] = "-"
    current_cell = area[new_r][new_c]

    if current_cell.isdigit():
        fish += int(current_cell)
        area[new_r][new_c] = "-"
    elif current_cell == "W":
        fish = 0
        ship_is_sink = True
        ship_pos = [new_r, new_c]
        break

    area[new_r][new_c] = "S"
    ship_pos = [new_r, new_c]

diff = 20 - fish
if ship_is_sink:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship_pos[0]},{ship_pos[1]}]")
elif fish >= 20:
    print("Success! You managed to reach the quota!")
    print(f"Amount of fish caught: {fish} tons.")
    for a in area:
        print(''.join(a))

else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {diff} tons of fish more.")
    if fish > 0:
        print(f"Amount of fish caught: {fish} tons.")
    for a in area:
        print(''.join(a))
