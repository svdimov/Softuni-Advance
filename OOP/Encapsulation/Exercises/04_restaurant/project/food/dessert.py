from project.food.food import Food
class Dessert(Food):
    def __init__(self,name:str,price:float,grams:float,calories:float):
        self.__calories = calories
        # Food.__init__(self,name,price,grams)
        super().__init__(name, price, grams)



    @property
    def calories(self):
        return self.__calories


