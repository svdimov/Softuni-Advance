class Glass:
    capacity = 250
    def __init__(self,content = 0):
        self.content = content

    def fill(self,ml):

        if (self.content + ml) > self.capacity:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"


    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        left = self.capacity - self.content
        return f"{left} ml left"




glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

