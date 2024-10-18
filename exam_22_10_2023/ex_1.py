from collections import deque

fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())

fuel_needed = deque(int(x) for x in input().split())
altitude = 0
result = 0
reached_altitude = []
while fuel and consumption_index and fuel_needed:
    current_fuel = fuel.pop()
    current_index = consumption_index.popleft()
    current_f_needed = fuel_needed.popleft()


    result = current_fuel - current_index
    if result >= current_f_needed:
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
        reached_altitude.append(f'Altitude {altitude}')

    else:
        print(f"John did not reach: Altitude {altitude+1}")
        fuel_needed.append(current_f_needed)
        break


if not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if reached_altitude:
        print(F"Reached altitudes: {', '.join(reached_altitude)}")
    else:
        print("John didn't reach any altitude.")


