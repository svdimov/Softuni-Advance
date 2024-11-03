from project.person import Person


class Child(Person):
    def __init__(self,name:str,age:int):
        Person.__init__(self,name,age)
