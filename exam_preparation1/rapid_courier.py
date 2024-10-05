from collections import deque



weight_package = [int(x) for x in input().split()]
courier_capacity = deque(int(x) for x in input().split())

total_weight = []


while courier_capacity and weight_package:
    capacity = courier_capacity.popleft()
    wight = weight_package[-1]

    if capacity >= wight:
        total_weight.append(wight)
        weight_package.pop()

        if capacity > wight:
            new_capacity = capacity - (wight * 2)
            if new_capacity > 0:
                courier_capacity.append(new_capacity)


    else:
        total_weight.append(capacity)
        wight-=capacity
        weight_package[-1] = wight


print(f"Total weight: {sum(total_weight)} kg")

if not weight_package and  not courier_capacity:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif weight_package and not courier_capacity:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x)for x in weight_package)}")
elif courier_capacity and not weight_package:
    print(f"Couriers are still on duty: {', '.join(str(x)for x in courier_capacity)} but there are no more packages to deliver.")





