#-----------RUNTIME ERROR
m = [1,2,3,4,5,6,7,8,9,10]

index = int(input())

try:
    print(m[index])
except IndexError:
    print('Index out of range ')

