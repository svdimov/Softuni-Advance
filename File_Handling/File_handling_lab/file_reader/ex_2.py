with open("numbers.txt") as file:
    content = file.read()
    split_content = content.split('\n')
    total_sum = 0
    for el in split_content:
        try:
            total_sum+=int(el)
        except ValueError:
            continue

print(total_sum)