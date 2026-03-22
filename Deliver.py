class Deliver:
    def __init__(self, order_id, address, distance, price, is_delivered):
        self.order_id = order_id
        self.address = address
        self.distance = distance
        self.price = price
        self.is_delivered = is_delivered

    def calculate_price(self):
        self.price = self.dectance * 2
        print(f"Uptate price: ${self.price}")

    def mark_delivered(self):
        self.is_delivered = True
        print("Delivery marked as delivered.")

    def update_address (self, new_address):
        self.address = new_address
        print(f"Updated address: {new_address}")

    def get_status(self):
        status = "Delivered" if self.is_delivered else "Not Delivered"
        return f"Order ID: {self.order_id}, Address: {self.address}, Price: ${self.price}, Status: {status}"