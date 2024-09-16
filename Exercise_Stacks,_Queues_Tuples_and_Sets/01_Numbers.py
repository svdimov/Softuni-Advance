sequences1 = set(int(x) for x in input().split())
sequences2 = set(int(x) for x in input().split())

for _ in range(int(input())):
    cmd = input().split()
    command = f'{cmd[0]} {cmd[1]}'
    number = [int(x) for x in cmd[2:]]
    if command == "Add First":
        sequences1.update(number)
    elif command == "Add Second":
        sequences2.update(number)
    elif command == "Remove First":
        sequences1.difference_update(number)
    elif command == "Remove Second":
        sequences2.difference_update(number)
    elif command == "Check Subset":
        print(sequences1.issubset(sequences2) or sequences2.issubset(sequences1))

print(*sorted(sequences1),sep=', ')
print(*sorted(sequences2),sep=', ')
