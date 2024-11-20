class dictionary_iter:
    def __init__(self,obj:dict):
        self.obj = tuple(obj.items())
        self.counter = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.obj):
            counter = self.counter # this is not the same variable
            self.counter+=1

            # return self.obj[self.counter-1]
            return self.obj[counter]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)