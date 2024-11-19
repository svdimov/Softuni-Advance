class reverse_iter:
    def __init__(self, obj):
        self.data = obj
        # self.end_inx = len(self.data) #case 1
        self.iter_obj = reversed(obj)

    # def __iter__(self):  #case 1
    #     return self
    #
    # def __next__(self):
    #     self.end_inx -= 1
    #     if self.end_inx >=0:
    #         return self.data[self.end_inx]
    #     raise StopIteration


    # def __iter__(self): case 2
    #     return reversed(self.data) #two time interation in for loop
    def __iter__(self):
        return self.iter_obj   # one time interation in for loop



reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

for item in reversed_list:
    print(item)