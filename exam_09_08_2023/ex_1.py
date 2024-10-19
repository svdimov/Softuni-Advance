from collections import deque

monster = deque(int(x) for x in input().split(','))
soldier = [int(x) for x in input().split(',')]
killed = 0

while monster and soldier:
    monster_armor = monster.popleft()
    soldier_strike = soldier.pop()

    if soldier_strike >= monster_armor:
        killed += 1
        soldier_strike -= monster_armor
        if soldier_strike > 0:
            if soldier:
                soldier[-1] += soldier_strike
                continue
            soldier.append(soldier_strike)

    else:
        monster_armor -= soldier_strike
        monster.append(monster_armor)

if not monster:
    print("All monsters have been killed!")
if not soldier:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed}")

