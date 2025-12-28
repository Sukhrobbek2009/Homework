class Movie:
    min_rating = 5
    
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def show_rating(self):
        print(f"Movie'{self.title}': Rating'{self.rating}'")

    @classmethod
    def change_min_rating(cls, value):
        cls.min_rating = value

    @staticmethod
    def is_good_movie(rating):
        if rating > 7:
            return "Good Movie"
        else:
            return "Not Recomding this movie"
