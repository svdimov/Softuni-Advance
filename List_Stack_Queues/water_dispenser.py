# from collections import deque
#
# queue = deque()
# litters = int(input())
#
# while True:
#     names = input()
#     if names == "Start":
#         break
#     queue.append(names)
#
# while True:
#     command = input().split()
#
#     if command[0] == "End":
#         break
#
#     if command[0] == "refill":
#         refill_liter = int(command[1])
#         litters += refill_liter
#
#     else:
#         needed_litters = int(command[0])
#         person = queue.popleft()
#         if litters >= needed_litters:
#             litters -= needed_litters
#             print(f'{person} got water')
#         else:
#             print(f'{person} must wait')
# print(f"{litters} liters left")
from collections import deque

def dispenser(litters,queue):
    while True:
        names = input()
        if names == "Start":
            break
        queue.append(names)

    while True:
        command = input().split()

        if command[0] == "End":
            break

        if command[0] == "refill":
            refill_liter = int(command[1])
            litters += refill_liter

        else:
            needed_litters = int(command[0])
            person = queue.popleft()
            if litters >= needed_litters:
                litters -= needed_litters
                print(f'{person} got water')
            else:
                print(f'{person} must wait')
    print(f"{litters} liters left")

queue = deque()
litters = int(input())
dispenser(litters,queue)