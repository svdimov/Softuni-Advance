class Shop:
    def __init__(self,name:str,items:list):
        self.items = items
        self.name = name


    def get_items_count(self) -> int:

        return len(self.items)



shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())