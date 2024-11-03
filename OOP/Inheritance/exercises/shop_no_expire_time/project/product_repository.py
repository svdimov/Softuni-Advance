from typing import Optional

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        # for p  in self.products:
        #     if p.name == product_name:
        #         return p
        #     return None
        return next((p for p in self.products if p.name == product_name), None)
        # некст метода е по-бърз при по-големи колекциа от  данни
        # вместо фор-цикъла

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        formatted = [f"{p.name}: {p.quantity}" for p in self.products]
        return '\n'.join(formatted)
