num = int(input())
even_set = set()
odd_set = set()
for row in range(1,num+1):
    names = input()
    sum_char = sum(ord(ch) for ch in names) // row
    if sum_char % 2 == 0:
        even_set.add(sum_char)
    else:
        odd_set.add(sum_char)

if sum(even_set) == sum(odd_set):
    print(*even_set|odd_set,sep=', ')
elif sum(odd_set) >  sum(even_set):
    print(*odd_set-even_set,sep=', ')
else:
    print(*even_set^odd_set,sep=', ')