

n = int(input())
stack = []
for _ in range(n):
    num = input().split()
    command = int(num[0])
    if command == 1:
        n2 = int(num[1])
        stack.append(n2)
    elif command == 2:
        if stack:
            stack.pop()
        else:
            continue
    elif command == 3:
        if stack:
            print(max(stack))
        else:
            continue

    elif command == 4:
        if stack:
            print(min(stack))
        else:
            continue

print(', '.join(map(str,stack[::-1])))
