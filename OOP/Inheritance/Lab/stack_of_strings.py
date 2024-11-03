class Stack:
    def __init__(self, *args):
        self.data = [str(el) for el in args]

    def push(self, element):
        self.data.append(str(element))

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True
    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"

s = Stack(1,2,3)
s.push(9)
s.push(25)
print(s)
print(s.pop())
print(s)
print(s.top())
for n in range(4):
    print(s.pop())
print(s.is_empty())