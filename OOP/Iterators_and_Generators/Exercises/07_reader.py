from typing import Iterable
def read_next(*args:Iterable):
    for collections in args:
        for el in collections:
            yield el










#
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print("=============================")
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)