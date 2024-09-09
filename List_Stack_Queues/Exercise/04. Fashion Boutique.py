

box_of_clothes = list(map(int,input().split()))
capacity = int(input())


count = 0
while box_of_clothes:
    count+=1
    current_capacity = capacity
    while box_of_clothes and box_of_clothes[-1]<=current_capacity:
        current_capacity-= box_of_clothes.pop()

print(count)