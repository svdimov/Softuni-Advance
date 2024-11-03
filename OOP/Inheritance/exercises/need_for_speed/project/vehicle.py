class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self,kilometers):
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel-= kilometers * self.fuel_consumption

