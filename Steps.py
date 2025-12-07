class Person:

    def __init__(self, name, steps_today, step):
        self.name = name
        self.steps_today = steps_today
        self.step = step

    def add_steps(self, count):
        self.steps_today += count

    def goal_reached(self, goal):
        if self.steps_today > goal:
            "True"
        else:
            "False"