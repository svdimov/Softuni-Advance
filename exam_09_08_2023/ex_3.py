def accommodate_new_pets(capacity: int, maximum_weight: float, *elements):
    pets = {}
    result = []
    for pet, kg in elements:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if maximum_weight < kg:
            continue
        if pet not in pets:
            pets[pet] = 1
        else:
            pets[pet] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    sorted_pets = sorted(pets.items())

    result.append("Accommodated pets:")
    for pets, num in sorted_pets:
        result.append(f"{pets}: {num}")
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
