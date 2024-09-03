parentheses = input()
my_stack = []
for i in range(len(parentheses)):
    if parentheses[i] == "(":
        my_stack.append(i)
    elif parentheses[i] == ")":
        recent_stack = my_stack.pop()
        print(parentheses[recent_stack:i+1])


