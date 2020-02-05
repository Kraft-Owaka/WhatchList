from app import create_app,bd
from . import db
from app.models import User



class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,movie_id,title,overview,poster,vote_average,vote_count):
        self.movie_id =movie_id
        self.title = title
        self.overview = overview
        self.poster = "http://image.tmdb.org/t/p/w500/"+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
class Review:
    all_reviews = []
    def __init__(self,movie_id,title,imageurl,Review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = Review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,movie_id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == movie_id:
                response.append(review)
        
                return response

class User (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

    @manager.shell
    def make_shell_context():
        return dict(app = app,db = db,User = User )
    if __name__ == '__main__':
        manager.run()
 
 