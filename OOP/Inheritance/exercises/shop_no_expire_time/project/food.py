from project.product import Product


class Food(Product):
    def __init__(self, name: str, quantity=15):
        Product.__init__(self, name, quantity)
