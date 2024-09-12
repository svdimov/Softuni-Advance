# set{} - неподредена колекция/unorder/  праменяща се
# a = set([1, 2, 3, 4])
# b = set([3, 4, 5, 6])
# a.union(b)  # Equivalent to a | b
# a.intersection(b)  # Equivalent to a & b
# a.issubset(b)  # Equivalent to a <= b
# a.issuperset(b)  # Equivalent to a >= b
# a.difference(b)  # Equivalent to a - b
# a.symmetric_difference(b)
# print(a.union(b))
# print(a.intersection(b))
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.difference(b))
# tuple() подредена колекция не  непроменеща се
# from copy import deepcopy
#
# a = [[1, 2],[3,4]]
# b = a.copy()
# c = deepcopy(a) # копира на всички нива във памета
# a =(2,1,2,3)
# print(a.count(2))
# print(a.index(2))
# a = ([1,2],[3,4]) # обиктите във тупъл са променящи
# a[0].append(5)
# a[0][0] = 100
# print(a)
# tuple unpacking
# a,b = (1,2)
# print(a)
# print(b)
