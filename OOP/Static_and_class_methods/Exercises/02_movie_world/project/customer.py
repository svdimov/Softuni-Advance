from project.dvd import DVD
class Customer:

    def __init__(self,name:str,age:int,_id:int):
        self.id = _id
        self.age = age
        self.name = name
        self.rented_dvds:list[DVD] = []


    def __repr__(self):
        titles = ', '.join([d.name for d in self.rented_dvds])
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({titles})"
