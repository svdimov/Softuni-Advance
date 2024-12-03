from project import Customer
from project import Equipment
from project import Subscription
from project import Trainer
from project import ExercisePlan


class Gym:

    def __init__(self):
        self.customers:list[Customer] = []
        self.trainers:list[Trainer] = []
        self.equipment:list[Equipment] = []
        self.plans:list[ExercisePlan] = []
        self.subscriptions:list[Subscription] = []
    # DONT REPEAT YOURSELF
    @staticmethod
    def add_object(obj,collection:list):
        if obj not in collection:
            collection.append(obj)

    def add_customer(self,customer: Customer):
        self.add_object(customer,self.customers)

    def add_trainer(self,trainer: Trainer):
        self.add_object(trainer,self.trainers)

    def add_equipment(self,equipment: Equipment):
        self.add_object(equipment, self.equipment)

    def add_plan(self,plan: ExercisePlan):
        self.add_object(plan,self.plans)
    def add_subscription(self,subscription: Subscription) :
        self.add_object(subscription, self.subscriptions)

    def subscription_info(self,subscription_id: int) :
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subscription_id),None)
        trainer = next((t for t in self.trainers if t.id == subscription_id),None)
        equipment = next((e for e in self.equipment if e.id == subscription_id),None)
        plan = next((p for p in self.plans if p.id == subscription_id),None)
        return  '\n'.join([subscription.__repr__(),
                            customer.__repr__(),
                            trainer.__repr__(),
                            equipment.__repr__(),
                            plan.__repr__()
        ])
