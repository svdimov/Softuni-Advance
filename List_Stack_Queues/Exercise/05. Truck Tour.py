from collections import deque

n_pmps = int(input())
kolonka = deque()
stops = 0
for _ in range(n_pmps):
    command = input().split()
    petrol = int(command[0])
    distance = int(command[1])
    kolonka.append([petrol, distance])

start_position = 0
stops = 0

while stops < n_pmps:

    fuel = 0
    for i in range(n_pmps):
        fuel += kolonka[i][0]
        destination = kolonka[i][1]
        if fuel < destination:
            kolonka.rotate(-1)
            start_position+=1
            stops =0
            break
        fuel -= destination
        stops += 1

print(start_position)
