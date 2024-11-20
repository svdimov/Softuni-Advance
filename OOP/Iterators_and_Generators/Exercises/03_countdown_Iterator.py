class countdown_iterator:
    def __init__(self,count):
        self.count = count+1
        self.i = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            self.i+=1
            return self.count - self.i
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
#
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")