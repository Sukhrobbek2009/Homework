store = {
    "banana": {"price": 2.0, "quantity": 10},
    "apple": {"price": 1.5, "quantity": 15},
    "milk": {"price": 3.0, "quantity": 8},
    "bread": {"price": 2.5, "quantity": 5}
}

class Custumer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)
        self.cart = []

    def add_product(self, product_name, quantity):
        if product_name in store:
            if store[product_name]["quantity"] >= quantity:
                self.cart.append((product_name, quantity))
                print(f"{quantity} {product_name}(s) added to cart.")
            else:
                print('Not enough quantity in store.')
        else:
            print('Product not found.')

    def total(self):
        total_cost = 0
        for product, quantity in self.cart:
            price = store[product]["price"]
            total_cost += price * quantity
        return total_cost
    
    def buy(self):
        total_cost = self.total()

        if self.balance >= total_cost:
            self.balance -= total_cost

            for product, quantity in self.cart:
                store[product]['quantity'] -= quantity

            print("Purchase successful!")
            print("Remaining balnce:", self.balance)
            self.cart.clear()
        else:
            print("Not enough balance.")