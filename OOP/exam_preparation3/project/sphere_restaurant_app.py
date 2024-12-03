from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    waiter_types = {'FullTimeWaiter': FullTimeWaiter, 'HalfTimeWaiter': HalfTimeWaiter}
    client_types = {'RegularClient': RegularClient, 'VIPClient': VIPClient}

    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        valid_waiter_name = next((n for n in self.waiters if n.name == waiter_name), None)
        if waiter_type not in self.waiter_types:
            return f"{waiter_type} is not a recognized waiter type."
        if valid_waiter_name:
            return f"{waiter_name} is already on the staff."

        waiter = self.waiter_types[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        valid_client = next((c for c in self.clients if c.name == client_name), None)
        if client_type not in self.client_types:
            return f"{client_type} is not a recognized client type."
        if valid_client:
            return f"{client_name} is already a client."

        client = self.client_types[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return waiter.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            client_points = client.earning_points(order_amount)
            return f"{client_name} earned {client_points} points from the order."

        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        client = next((c for c in self.clients if c.name == client_name), None)

        if client:
            client_discount = client.apply_discount()

            return f"{client_name} received a {client_discount[0]}% discount. Remaining points {client_discount[1]}"

        return f"{client_name} cannot get a discount because this client is not admitted!"

    #
    def generate_report(self):
        total_earnings = sum([w.calculate_earnings() for w in self.waiters])  # TDOD :.2f
        total_client_points = sum([c.points for c in self.clients])
        # sorted_waiters = sorted(self.waiters,key=lambda w: w.calculate_earnings,reverse=True)
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)
        result = "$$ Monthly Report $$\n"
        result += f"Total Earnings: ${total_earnings:.2f}\n"
        result += f"Total Clients Unused Points: {total_client_points}\n"
        result += f"Total Clients Count: {len(self.clients)}\n"

        result += "** Waiter Details **\n"
        for waiters in sorted_waiters:
            result += waiters.__str__() + '\n'

        return result.strip()
        # return result[:-1]


# Create an instance of SphereRestaurantApp
sphere_restaurant_app = SphereRestaurantApp()

# Hire some waiters
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))

# Admit some clients
print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))

# Process shifts
print(sphere_restaurant_app.process_shifts("John"))
print(sphere_restaurant_app.process_shifts("Alice"))
print(sphere_restaurant_app.process_shifts("Emily"))
print(sphere_restaurant_app.process_shifts("Frank"))

# Process client orders
print(sphere_restaurant_app.process_client_order("Bob", 100.0))
print(sphere_restaurant_app.process_client_order("Eve", 500.0))
print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
print(sphere_restaurant_app.process_client_order("Bob", 750.0))
print(sphere_restaurant_app.process_client_order("Lila", 550.0))
print(sphere_restaurant_app.process_client_order("Oscar", 84.0))

# Apply discounts to clients
print(sphere_restaurant_app.apply_discount_to_client("Lila"))
print(sphere_restaurant_app.apply_discount_to_client("Eve"))
print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
print(sphere_restaurant_app.apply_discount_to_client("Bob"))

# Generate report
print(sphere_restaurant_app.generate_report())
