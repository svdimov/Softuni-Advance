from project import Product


class Beverage(Product):
    def __init__(self,name:str,price:float,milliliters:float):
        self.__milliliters = milliliters
        # Product.__init__(self,name,price)
        super().__init__(name,price)

    @property
    def milliliters(self):
        return self.__milliliters
