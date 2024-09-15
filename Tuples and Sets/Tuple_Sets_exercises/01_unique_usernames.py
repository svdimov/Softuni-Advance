unique_name = set()

for _ in range(int(input())):
    names = input()
    unique_name.add(names)
print(*unique_name,sep='\n')