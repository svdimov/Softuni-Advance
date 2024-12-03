from project import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        Animal.__init__(self,name,age,gender)



    def make_sound(self):
        return "Woof!"


    def __repr__(self):
        # return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
        return self.repr(self.name, self.age, self.gender, self.__class__.__name__)

