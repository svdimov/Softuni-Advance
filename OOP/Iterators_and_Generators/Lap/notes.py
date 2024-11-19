# INTERATORS __iter__ and __next__
# class Person:
#     def __init__(self,name:str):
#         self.name = name
#         self.current_inx = -1
#
#     def __len__(self):
#         return len(self.name)
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_inx+=1
#         if self.current_inx < len(self.name):
#             return self.name[self.current_inx]
#         raise StopIteration
#
# p = Person('Test')
# GENERATORS -----yield--------

# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num+=1
#
# res = first_n(5)
# for el in res:
#     print(el)
#
#
# def m_gen():
#     n = 1
#     print("that is first")
#     yield n
#
#     n += 1
#     print('that is second')
#     yield n
#
#     n += 1
#     print('that is last')
#     yield n
#
#
# rs = m_gen()
# for e in rs:
#     print(e)
# за повече интерации на генератора зануляваме
# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
#
# res = first_n(5)
# for el in res:
#     print(el)
# res = first_n(5)
# for el in res:
#     print(el)
# за повече интерации на инератора зануляваме
class FirstN:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self  # The object itself is the iterator.

    def __next__(self):
        if self.current < self.n:
            result = self.current
            self.current += 1
            return result

        raise StopIteration  # Signal that iteration is complete.

# Create an instance of the iterator and loop through it for the first time
res = FirstN(5)
for el in res:
    print(el)

# Create a new instance to iterate again
res = FirstN(5)
for el in res:
    print(el)
