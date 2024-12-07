from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.robots.base_robot import BaseRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    robots_type = {'FemaleRobot': FemaleRobot, 'MaleRobot': MaleRobot}
    service_type = {'MainService': MainService, 'SecondaryService': SecondaryService}

    def __init__(self):
        self.robots:list[BaseRobot] = []
        self.services:list[BaseService] = []

    def add_service(self, _type: str, name: str):
        if _type == "MainService":
            service = MainService(name)
        elif _type == "SecondaryService":
            service = SecondaryService(name)
        else:
            raise Exception("Invalid service type!")
        self.services.append(service)
        return f"{_type} is successfully added."

    def add_robot(self, _type: str, name: str, kind: str, price: float):
        if _type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif _type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")
        self.robots.append(robot)
        return f"{_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(r for r in self.robots if r.name == robot_name)
        service = next(s for s in self.services if s.name == service_name)

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."
        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."
        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(s for s in self.services if s.name == service_name)
        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join(service.details() for service in self.services)

main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
