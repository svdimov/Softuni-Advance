from project import Animal


class Cat(Animal):

    def __init__(self, name: str, age: int, gender: str):
        Animal.__init__(self,name,age,gender)



    def make_sound(self):
        return "Meow meow!"


    def __repr__(self):
        # DON'T REPEAT YOURSELF
        # return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
        return self.repr(self.name,self.age,self.gender,self.__class__.__name__)


