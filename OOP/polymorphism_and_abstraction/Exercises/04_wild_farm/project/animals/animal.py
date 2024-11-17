from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @property
    @abstractmethod
    def allowed_food(self) -> list[Food]:
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def weight_increment(self) -> float:
        pass

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.weight_increment
        self.food_eaten += food.quantity




class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size: float):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"



class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region: str):
        Animal.__init__(self, name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

