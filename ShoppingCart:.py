class ShoppingCart:
    def __init__(self, item):
        self.item = item

    def add_item(self, item, price):
        self.item =item
        self.price = price

    def remove_item(self, item):
        if item in self.item:
            del self.item[item]
        else:
            print(f"{item} not found in cart")

    def total(self):
        return sum(self.item.values())
    