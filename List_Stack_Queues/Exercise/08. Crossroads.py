from collections import deque

# Input for green light and free window durations
green_light = int(input())
window_pass = int(input())

# Queue to hold the cars at the intersection
cars = deque()

# Initialize variables to keep track of the total number of cars passed and if a crash occurred
passed_cars = 0

crash_happened = False

while True:
    command = input()

    # Stop the simulation when "END" is received
    if command == "END":
        break

    # Handle the green light command
    elif command == "green":
        current_green_light = green_light

        # Using a for loop to process each car in the queue
        for _ in range(len(cars)):
            if current_green_light <= 0:  # Stop processing if green light time is exhausted
                break

            car = cars.popleft()  # Remove the car from the front of the queue
            car_length = len(car)

            if car_length <= current_green_light:
                # The car passes completely within the green light duration
                current_green_light -= car_length
                passed_cars += 1
            else:
                # The car can only partially pass; check if it fits in the free window
                remaining_car_length = car_length - current_green_light
                if remaining_car_length <= window_pass:
                    # The car passes completely within the free window
                    passed_cars += 1
                else:
                    # The car crashes
                    indx = current_green_light + window_pass
                    print("A crash happened!")
                    print(f"{car} was hit at {car[indx]}.")
                    crash_happened = True
                    break

                # The green light is completely used up at this point
                current_green_light = 0

        # Exit the loop if a crash occurred
        if crash_happened:
            break

    else:
        # A car arrives at the crossroads, add it to the queue
        cars.append(command)

# Final output after processing all commands
if not crash_happened:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
