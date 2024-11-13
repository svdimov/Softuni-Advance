from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self,name:str,age:int,gender:str):
        self.name = name
        self.age = age
        self.gender = gender


    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def repr(name, age, gender, class_name):
        return f"This is {name}. {name} is a {age} year old {gender} {class_name}"

