class ClsMixin:
    id = 1

    @classmethod
    def increments_id(cls):
        cls.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id



