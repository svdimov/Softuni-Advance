from project import Mammal
from project import Meat,Vegetable,Fruit


class Mouse(Mammal):

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def weight_increment(self):
        return 0.10

class Dog(Mammal):

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof"

    @property
    def weight_increment(self):
        return 0.40

class Cat(Mammal):

    @property
    def allowed_food(self):
        return [Vegetable,Meat]

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def weight_increment(self):
        return 0.30

class Tiger(Mammal):

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def weight_increment(self):
        return 1.00

