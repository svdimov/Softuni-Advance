from project import Animal
from project import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.workers: list[Worker] = []
        self.animals: list[Animal] = []
        self.__workers_capacity = worker_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        current_worker = next((w for w in self.workers if w.name == worker_name), None)
        if current_worker:
            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salary_workers = sum(w.salary for w in self.workers)
        if self.__budget < salary_workers:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salary_workers
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        care_animals = sum(a.money_for_care for a in self.animals)
        if self.__budget < care_animals:  #
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= care_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"



    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):

        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

        # tigers = []
        # cheetahs = []
        # for animals in self.animal:
        #     if animals.__class__.__name__ == "Lion":
        #         lions.append(repr(animals))
        #     elif animals.__class__.__name__ == "Tiger":
        #         tigers.append(repr(animals))
        #     elif animals.__class__.__name__ == "Cheetah":
        #         cheetahs.append(repr(animals))
        #
        # result = [f"You have {len(self.animal)} animals", f"----- {len(lions)} Lions:"]
        # result.extend(lions)
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(cheetahs)
        #
        # return "\n".join(result)

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    @staticmethod
    def __print_status(obj_list: list[Animal | Worker], *class_names: str):
        elements = {name: [] for name in class_names}
        for obj in obj_list:
            elements[obj.__class__.__name__].append(repr(obj))
        result = [f"You have {len(obj_list)} {str(obj_list[0].__class__.__bases__[0].__name__).lower()}s"]
        for k, v in elements.items():
            result.append(f"----- {len(v)} {k}s:")
            result.extend(v)
        return "\n".join(result)
