from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
presents = {}
items = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'

}

while materials and magic_level:
    magic_needed = materials[-1] * magic_level[0]
    if magic_needed in items:
        current_present = items[magic_needed]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
        materials.pop()
        magic_level.popleft()

    elif magic_needed < 0:
        materials.append(magic_level.popleft() + materials.pop())

    elif magic_needed > 0:
        magic_level.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0: materials.pop()
        if magic_level[0] == 0: magic_level.popleft()

if ('Doll' in presents and 'Wooden train' in presents) or \
        ('Teddy bear' in presents and 'Bicycle' in presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
for k, v in sorted(presents.items()):
    print(f"{k}: {v}")
