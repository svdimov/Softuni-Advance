from collections import deque
bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
operator = deque(input().split())
honey = 0

def calk(bees, nectar, operator):
    if operator == '+':
        return abs(bees + nectar)
    elif operator == '-':
        return  abs(bees - nectar)
    elif operator == '*':
        return abs(bees * nectar)
    elif operator == '/':
        if  nectar == 0:
            return 0
        else:
            return abs(bees / nectar)

while bees and nectar:
    if nectar[-1] >= bees[0]:
        op = operator.popleft()
        bee = bees.popleft()
        n = nectar.pop()
        honey += calk(bee,n,op)
    else:
        nectar.pop()
print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")



