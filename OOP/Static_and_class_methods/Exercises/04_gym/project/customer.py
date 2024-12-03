from project import ClsMixin


class Customer(ClsMixin):

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.email = email
        self.address = address
        self.id = self.get_next_id()
        self.increments_id()


    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
