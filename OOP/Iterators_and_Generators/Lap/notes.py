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
#

