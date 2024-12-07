from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 30, 'MainService')

    def details(self):

        # robots_info = " ".join(robot.name for robot in self.robots) if self.robots else "none"
        # return f"{self.name} Main Service:\nRobots: {robots_info}"
        r_name = [r.name for r in self.robots]
        if self.robots:
            return f"{self.name} Main Service:\nRobots: {' '.join(r_name)}"
        return f"{self.name} Main Service:\nRobots: none"
