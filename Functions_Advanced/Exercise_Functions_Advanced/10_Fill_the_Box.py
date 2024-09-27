def fill_the_box(height, length, width, *args):
    box_size = height*length*width
    cubes = 0
    for element in args:
        if element == "Finish":
            break

        cubes+=element
    diff = abs(box_size-cubes)
    if box_size > cubes:
        return f"There is free space in the box. You could put {diff} more cubes."
    return f"No more free space! You have {diff} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))