from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())

total_goal = 0
sum_kick = 0

while strength and accuracy:
    current_strength = strength[-1]
    current_accuracy = accuracy[0]

    sum_kick = current_strength + current_accuracy
    if sum_kick == 100:
        total_goal += 1
        strength.pop()
        accuracy.popleft()
    elif sum_kick < 100:
        if current_strength < current_accuracy:
            strength.pop()
        elif current_strength > current_accuracy:
            accuracy.popleft()
        else:
            strength[-1] = current_strength + current_accuracy
            accuracy.popleft()

    elif sum_kick > 100:
        current_strength-=10
        strength.pop()
        accuracy.popleft()
        strength.append(current_strength)
        accuracy.append(current_accuracy)




if total_goal == 3:
    print("Paul scored a hat-trick!")
elif total_goal == 0:
    print("Paul failed to score a single goal.")

elif total_goal > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")
if total_goal:
    print(f"Goals scored: {total_goal}")

if strength:
    print(f"Strength values left: {', '.join(str(x) for x in strength)}")
else:
    pass

if accuracy:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy)}")
