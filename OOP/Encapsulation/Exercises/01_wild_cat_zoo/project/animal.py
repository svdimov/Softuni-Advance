
class Animal:

    def __init__(self,name:str,gender:str,age:int,money_for_care:int):
        
        self.money_for_care = money_for_care
        self.age = age
        self.gender = gender
        self.name = name

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
