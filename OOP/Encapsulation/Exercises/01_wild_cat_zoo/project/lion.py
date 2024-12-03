from project import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        Animal.__init__(self,name,gender,age,money_for_care=50)



