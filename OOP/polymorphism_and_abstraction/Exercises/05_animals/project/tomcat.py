from project.cat import Cat
class Tomcat(Cat):

    def __init__(self,name,age):
        Cat.__init__(self,name,age,'Male')



    def make_sound(self):
        return "Hiss"

    def __repr__(self):
        # return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
        return self.repr(self.name, self.age, self.gender, self.__class__.__name__)
