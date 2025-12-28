class Player:
    max_level = 100

    def __init__(self, username, level):
        self.username = username
        self.level = level
        
    def level_up(self):
        self.level += 1

    @classmethod
    def show_max_level(cls):
        print("max level:",{cls.max_level})

    @staticmethod
    def is_valid_username(name):
        return len(name) >= 3