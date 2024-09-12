n, m = map(int, input().split())

set1 = {int(input()) for _ in range(n)}
set2 = {int(input()) for _ in range(m)}

print(*set1.intersection(set2), sep='\n')

print(type(set1))