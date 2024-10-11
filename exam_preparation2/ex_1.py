from collections import deque

bee_group = deque(int(x) for x in input().split())
attackers_group = [int(x) for x in input().split()]

while bee_group and attackers_group:
    bee = bee_group[0]
    attackers = attackers_group[-1]
    current_attacker = attackers*7

    if bee < current_attacker:
        modul = bee // 7
        current_attacker-= bee
        bee_group.popleft()
        if current_attacker > 0:
            attackers_group.pop()
            attackers_group.append(attackers-modul)

    elif bee > current_attacker:
        bee-= current_attacker
        attackers_group.pop()
        if bee > 0:
            bee_group.popleft()
            bee_group.append(bee)

    elif bee == current_attacker:
        bee_group.popleft()
        attackers_group.pop()

print("The final battle is over!")
if bee_group:
    print(f"Bee groups left: {', '.join(str(x)for x in bee_group)}")
if attackers_group:
    print(f"Bee-eater groups left: {', '.join(str(x)for x in attackers_group)}")

if len(bee_group) == 0 and len(attackers_group) == 0:
    print("But no one made it out alive!")









