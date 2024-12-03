from project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.5
    # def __init__(self,coffeine:float,name:str):
    def __init__(self, name: str,coffeine:float):
        self.__coffeine = coffeine
        # HotBeverage.__init__(self,name,self.PRICE,self.MILLILITERS)
        super().__init__(name, self.PRICE, self.MILLILITERS)
    @property
    def coffeine(self):
        return self.__coffeine