from abc import ABC, abstractmethod

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):

    def __init__(self,code: str, volume: int):
        self.volume = volume  # capacity
        self.code = code
        self.ships:list[BaseBattleship] = []
        self.type = None

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value:str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        battleships = sorted(self.ships,key=lambda ship: (-ship.hit_strength,ship.name))
        return battleships

    @abstractmethod
    def zone_info(self):
        pass
