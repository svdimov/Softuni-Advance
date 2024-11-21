class take_skip:
    def __init__(self,step:int,count:int):
        self.step = step
        self.count = count
        self.current_c = -1



    def __iter__(self):
        return self

    def __next__(self):
        self.current_c+=1
        if self.current_c < self.count:
            return self.step * self.current_c
        raise StopIteration



numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)