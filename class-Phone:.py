class Phone:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def top_up(self, amount):
        self.balance += amount
        print(f"{self.owner} topped up ${amount}. New balance: ${self.balance}")

    def call(self, cost):
        if self.balance < cost:
            print(f"Not enough money in balance to make call. You have ${self.balance}, but need ${cost}.")
        else:
            self.balance -= cost
            print(f"Call made! Cost: ${cost}. Remaining balance: ${self.balance}")

    def check_balance(self):
        print(f"{self.owner}'s current balance is: ${self.balance}")