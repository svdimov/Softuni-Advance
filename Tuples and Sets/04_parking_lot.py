list_in = set()

for _ in range(int(input())):
    command, tables = input().split(', ')

    if command == "IN":
        list_in.add(tables)
    elif command == "OUT":

        list_in.remove(tables)
if list_in:
    print(*list_in, sep="\n")
else:
    print("Parking Lot is Empty")
