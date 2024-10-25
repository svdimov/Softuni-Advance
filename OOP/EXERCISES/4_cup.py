class Cup:
    def __init__(self,size:int,quantity:int):
        self.quantity = quantity
        self.size = size

    def fill(self,quantity_of):

        if self.quantity + quantity_of <= self.size:
            self.quantity += quantity_of


    def status(self):
        return  self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())