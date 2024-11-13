from project.cls_mixin import ClsMixin


class Trainer(ClsMixin):

    def __init__(self,name:str):
        self.name = name
        self.id = self.get_next_id()
        self.increments_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
