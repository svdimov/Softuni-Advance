def boarding_passengers(ship_capacity, *passenger_groups):

    boarded_passengers = {}
    available_capacity = ship_capacity


    for group_size, benefit_program in passenger_groups:

        if group_size <= available_capacity:

            available_capacity -= group_size
            if benefit_program in boarded_passengers:
                boarded_passengers[benefit_program] += group_size
            else:
                boarded_passengers[benefit_program] = group_size

        if available_capacity == 0:
            break


    sorted_boarding_details = sorted(boarded_passengers.items(), key=lambda x: (-x[1], x[0]))


    result = "Boarding details by benefit plan:\n"
    for benefit_program, total_passengers in sorted_boarding_details:
        result += f"## {benefit_program}: {total_passengers} guests\n"


    if available_capacity == ship_capacity:
        result += f"Partial boarding completed. Available capacity: {available_capacity}."
    elif available_capacity == 0:
        if sum(group_size for group_size, _ in passenger_groups) == sum(boarded_passengers.values()):
            result += "All passengers are successfully boarded!"
        else:
            result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {available_capacity}."

    return result



# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), \
#                           (35, 'Gold'), (25, 'First Cruiser')))

# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'),\
#                           (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'),\
                          (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))