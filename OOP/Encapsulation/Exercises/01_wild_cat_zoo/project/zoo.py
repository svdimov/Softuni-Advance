from project.animal import Animal
from project.worker import Worker
from typing import Union

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.worker: list[Worker] = []
        self.animal: list[Animal] = []
        self.__worker_capacity = worker_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animal):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animal.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__worker_capacity <= len(self.worker):
            return "Not enough space for worker"
        self.worker.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        current_worker = next((w for w in self.worker if w.name == worker_name), None)
        if current_worker:
            self.worker.remove(current_worker)
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salary_workers = sum(w.salary for w in self.worker)
        if self.__budget <= salary_workers:  # TODO
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salary_workers
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        care_animals = sum(a.money_for_care for a in self.animal)
        if self.__budget <= care_animals:  # TODO
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= care_animals

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):

        return self.__print_status(self.animal, "Lion", "Tiger", "Cheetahs")
        # lions = []
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

    def __print_status(self, obj_list: list[Animal | Worker], *class_names: str):
        pass
