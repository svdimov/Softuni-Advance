from project.user import User
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan
from project.route import Route
from project.vehicles.base_vehicle import BaseVehicle

class ManagingApp:

    vehicle_types_dict = {'PassengerCar':PassengerCar,'CargoVan':CargoVan}

    def __init__(self):
        self.users:list[User] = []
        self.vehicles:list[BaseVehicle] = []
        self.routes:list[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        # if any(user.driving_license_number == driving_license_number for user in self.users):
        #     return f"{driving_license_number} has already been registered to our platform."
        user = next((u for u in self.users if u.driving_license_number==driving_license_number),None)
        if user:
            return f"{driving_license_number} has already been registered to our platform."


        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.vehicle_types_dict:
            return f"Vehicle type {vehicle_type} is inaccessible."

        # if any(vehicle.license_plate_number == license_plate_number for vehicle in self.vehicles):
        #     return f"{license_plate_number} belongs to another vehicle."
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number),None)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."



        vehicle = self.vehicle_types_dict[vehicle_type](brand, model, license_plate_number)

        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(u for u in self.users if u.driving_license_number == driving_license_number)
        vehicle = next(v for v in self.vehicles if v.license_plate_number == license_plate_number)
        route = next(r for r in self.routes if r.route_id == route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted(
            [v for v in self.vehicles if v.is_damaged],
            key=lambda x: (x.brand, x.model)
        )
        repaired_count = 0

        for vehicle in damaged_vehicles[:count]:
            vehicle.change_status()
            vehicle.recharge()
            repaired_count += 1

        return f"{repaired_count} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        return "*** E-Drive-Rent ***\n" + "\n".join(str(user) for user in sorted_users)


app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
