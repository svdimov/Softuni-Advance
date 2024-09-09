from collections import deque

expression = deque(input())

open_brackets = '([{'
closing_brackets = ')]}'
count = 0
# {[()]}
while expression and count < len(expression) /2:
    if expression[0] not in open_brackets:
        break
    index = open_brackets.index(expression[0])
    if expression[1] == closing_brackets[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(count)
        count = 0
    else:
        expression.rotate(-1)
        count+=1

if expression:
    print('NO')
else:
    print('YES')
