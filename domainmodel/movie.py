from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:

    def __init__(self, movie_full_name: str, movie_date: int):
        self.__description = None
        self.__director = None
        self.__actor = []
        self.__genre = []
        self.__minutes = None
        if movie_full_name == "" or type(movie_full_name) is not str:
            self.__movie_full_name = None
        else:
            self.__movie_full_name = movie_full_name.strip()
        if movie_date < 1900 or movie_date == "" or type(movie_date) is not int:
            self.__movie_full_name = None
        else:
            self.__movie_date = movie_date

    @property
    def __repr__(self):
        return f"<Movie {self.__movie_full_name}, {self.__movie_date}>"

    def __eq__(self, other):
        return self.__movie_full_name == other.movie_full_name and self.__movie_date == other.movie__date

    def __lt__(self, other):
        return (self.movie_date, self.movie_full_name) < (other.movie_date, other.movie_full_name)

    def __hash__(self):
        return hash(self.__movie_full_name, self.___movie_date)

    @property
    def movie_full_name(self) -> str:
        return self.__movie_full_name

    def movie_full_name(self, movie_full_name):
        if movie_full_name == "" or type(movie_full_name) is not str:
            self.__movie_full_name = None
        else:
            self.__movie_full_name = movie_full_name.strip()

    def movie_date(self) -> int:
        return self.__movie_date

    def movie_date(self, movie_date):
        if movie_date < 1900 or movie_date == "" or type(movie_date) is not int:
            self.__movie_full_name = None
        else:
            self.__movie_date = movie_date

    @property
    def description(self) -> str:
        return self.__description

    def description(self, description):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    def director(self):
        return self.__director

    def director(self, director):
        if type(director) is not Director:
            self.__director = None
        else:
            self.__director = director

    def actor(self):
        return self.__actor

    def actor(self, actor):
        if type(actor) is not list:
            self.__actor = []
        else:
            self.__actor = actor

    def genre(self):
        return self.__genre

    def genre(self, genre):
        if type(genre) is not list:
            self.__genre = []
        else:
            self.__genre = genre

    @property
    def minutes(self):
        return self.__minutes

    def minutes(self, minutes):
        if type(minutes) is not int or minutes < 1:
            raise ValueError
        else:
            self.__minutes = minutes

    def add_actor(actor):
        self.actor.append(actor)

    def remove_actor(actor):
        if actor in self.actor:
            self.actor.remove(actor)

    def add_genre(genre):
        self.genre.append(genre)

    def remove_genre(genre):
        if genre in self.genre:
            self.genre.remove(genre)