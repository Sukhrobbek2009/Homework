class Movie:
    total_movies = 0
    all_genres = {"Action", "Comedy", "Drama", "Horror", "Sci-Fi"}

    def __init__(self, title, director, rating, genre):
        self.title = title
        self.director = director
        self._rating = None
        self._genre = None

        self.rating = rating
        self.genre = genre

        Movie.total_movies += 1
   
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if Movie.is_valid_rating(value):
            self._rating = value
        else:
            self._rating = 0

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if Movie.is_valid_genre(value):
            self._genre = value
        else:
            self._genre = "Unknown"
    
    def update_rating(self, new_rating):
        self.rating = new_rating
    
    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Director: {self.director}\n"
            f"Rating: {self.rating}/10\n"
            f"Genre: {self.genre}"
        )
    
    @classmethod
    def get_total_movies(cls):
        return cls.total_movies

    @classmethod
    def from_string(cls, movie_string):
        title, director, rating, genre = movie_string.split("|")
        return cls(title, director, float(rating), genre)
    
    @staticmethod
    def is_valid_rating(rating):
        return 0 <= rating <= 10

    @staticmethod
    def is_valid_genre(genre):
        return genre in Movie.all_genres
