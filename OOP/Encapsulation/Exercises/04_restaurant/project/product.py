class Product:
    def __init__(self,name:str,price:float):
        self.__price = price
        self.__name = name
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

