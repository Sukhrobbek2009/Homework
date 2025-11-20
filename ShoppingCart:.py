class ShoppingCart:
    def __init__(self, item, price, items):
        self.item = item
        self.price = price
        self.items = items

    def add_item(self):
        self.item[self.item] = self.price

    def remove_item(self, item):
        if item in self.item:
            del self.item[item]
        else:
            print(f"{item} not found in cart")

    def total(self):
        return sum(self.item.values())
    