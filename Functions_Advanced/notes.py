# ----------- *args
# def sum_nums(*args):
#     total_sum = 0
#     for el in args:
#         total_sum+= el
#     return total_sum
#
#
# print() #
# print(sum_nums(20,15)) # packing - ПОДАВА СТОЙНОСТИ ВЪВ ТЮПЪЛИ



# ------------------ **kwargs

# def sum_nums(*args, **kwargs): # АРГС ВРЪЩА РЕЧНИК
#     total_sum = 0
#     for el in args:
#         total_sum+= el
#     for k,v in kwargs.items():
#         print(f"{k} {v}")
#
#     return total_sum
#
#
#
# print(sum_nums(10,15 , names = 'test', age = 20))

# # -----------------------DICTIONERY SORTED
# my_dict = {'Peter': 21, 'George':18, 'John': 45, 'Ivan': 45}
# result = sorted(my_dict.items(), key = lambda kvp: kvp[1], ) # сортира индекса по велюта от речника
# result2 = sorted(my_dict.items(), key = lambda kvp: (-kvp[1], kvp[0])) # сортира  по равна година но по азбучен ред спрямо името
# print(result)
# print(result2)
# ---------------------NESTED FUNCTIONS
# def outer_fuc(b):
#     x =7
#     def inner_func():
#         print(x)
#         print(b)
#     inner_func()
# outer_fuc(5)
# reduce(lambda x,y : x- y, args) редус винага взема два елемената 1 ламда 2 args
# --------------------RECURSION
# def count_10(num):
#     if num  == 10:
#         return num
#     return count_10(num+1)
# print(count_10(1))
# -----Factorial recursion
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(5))