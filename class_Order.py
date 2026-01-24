class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.item = {}

    def add_item(self, name, price):
        if price <= 0:
            return
        
        self.items[name] = price

    def get_total(self):
        return sum(self.items.values())
    
    def get_order_type(self):
        total = self.get_total()
        if total >= 100:
            print("Expensive Order")
        else:
            print("Normal Order")