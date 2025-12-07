class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100

    def work(self):
        if self.battery >= 10:
            self.battery -= 10
        else:
            print("Battery is too low")

    def recharge(self):
        self.battery = 100

    def status(self):
        print(f"{self.name}'s Battery name: {self.battery}")