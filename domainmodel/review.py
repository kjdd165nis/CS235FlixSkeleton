from datetime import datetime

from domainmodel.movie import Movie

class Review:
    def _init_(self, movie, review_text, rating):
        self.moive = movie
        self.review_text = review_text
        if rating > 10 or rating < 1:
            self.rating = None
        else:
            self.rating = rating
        self.timestamp = datetime.now()

    def __repr__(self):
        print(self.moive)
        return "Review: " + self.review_text + "\n" + "Rating: " + str(self.rating)

    def __eq__(self, other):
        if self.moive == other.movie and self.rating == other.rating and self.review_text == other.review_text and self.timestamp == other.timestamp:
            return True
        else:
            return False