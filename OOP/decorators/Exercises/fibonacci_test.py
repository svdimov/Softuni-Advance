
n = 10
a,b = 0,1

fib_list = []
for i in range(n):
   fib_list.append(a)
   a,b = b,a+b

print(*fib_list)

def fib (n2):
    if n2 <= 0:
        return n2
    elif n2 <= 1:
        return n2
    else:
        return fib(n2-1) + fib(n2-2)





n2 = 10
for i in range(n2):
    print(fib(i),end=' ')
