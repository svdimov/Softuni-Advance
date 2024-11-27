from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    product_types = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    store_types = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.product_types:
            raise Exception("Invalid product type!")
        # if product_type not in ['Chair','HobbyHorse']:
        # if product_type == "Chair":
        #     product = Chair(model,price)
        # else:
        #     product = HobbyHorse(model,price)
        # p_type = next((t for t in  self.products if t.sub_type == product_type),None)
        product = self.product_types[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):

        if store_type not in self.store_types:
            raise Exception(f"{store_type} is an invalid type of store!")
        store_product = self.store_types[store_type](name, location)
        self.stores.append(store_product)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_product = [p for p in products if p.sub_type == store.sells]
        if not filtered_product:
            return f"Products do not match in type. Nothing sold."

        for p in filtered_product:
            store.products.append(p)
            store.capacity -= 1
            self.products.remove(p)
            self.income += p.price
        return f"Store {store.name} successfully purchased {len(filtered_product)} items."

    def unregister_store(self, store_name: str):
        try:
            current_store = [s for s in self.stores if s.name == store_name][0]
        except IndexError:
            raise Exception("No such store!")
        if current_store.products:
            return f"The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(current_store)
        return f"Successfully unregistered store {current_store.name}, location: {current_store.location}."

    def discount_products(self, product_model: str):
        filter_products = [f for f in self.products if f.model == product_model]

        for p in filter_products:
            p.discount()
        return f"Discount applied to {len(filter_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        try:
            store = [s for s in self.stores if s.name == store_name][0]
            # store = [s.store_stats() for s in self.stores if s.name == store_name]
        except IndexError:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        result = f"Factory: {self.name}\n"
        result += f"Income: {self.income:.2f}\n"
        result += "***Products Statistics***\n"

        product_stats = {}
        for p in self.products:
            if p.model not in product_stats:
                product_stats[p.model] = 0
            product_stats[p.model] += 1

        result += (f"Unsold Products: {len(self.products)}. "
                   f"Total net price: {sum([p.price for p in self.products]):.2f}\n")
        order_products = sorted(product_stats)
        for model in order_products:
            result += f"{model}: {product_stats[model]}\n"

        result += f"***Partner Stores: {len(self.stores)}***\n"
        store_names = '\n'.join(sorted([s.name for s in self.stores]))
        result += store_names

        return result
