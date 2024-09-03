a = int(input())
my_list = []
for i in range(a,-1,-1):
    my_list.append(i)

even_list = [even for even in my_list if even % 2 == 0]
print(even_list)
print(my_list)