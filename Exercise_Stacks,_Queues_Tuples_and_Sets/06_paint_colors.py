from collections import deque


data = deque(input().split())
colors = ['red', 'yellow', 'blue','orange', 'purple', 'green']
color_made = []


def color_check(color, list_colors):
    if color == 'orange' and "red" in list_colors and 'yellow' in list_colors:
        return True
    elif color == "purple" and 'red' in list_colors and 'blue' in list_colors:
        return True
    elif color == 'green' and "yellow" in list_colors and 'blue' in list_colors:
        return True
    elif color == 'red' or color == 'yellow' or color == 'blue':
        return True
    else:
        return False


while data:
    first_str = data.popleft()
    last_str = data.pop() if data else ''
    for color in (first_str + last_str, last_str + first_str):
        if color in colors:
            color_made.append(color)
            break
    else:
        if len(first_str) > 1:
            data.insert(len(data) // 2, first_str[:-1])
        if len(last_str) > 1:
            data.insert(len(data) // 2, last_str[:-1])

for c in color_made:
    if not color_check(c,color_made):
        color_made.remove(c)

print(color_made)
