from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9, 'MaleRobot')

    def eating(self):
        self.weight += 3
