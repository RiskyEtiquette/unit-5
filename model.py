"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    @classmethod
    def create(cls, email, password):
        """Create and return a new user."""
        return cls(email=email, password=password)

    @classmethod
    def get_all(cls):
        """Return all users."""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, user_id):
        """Return a user by primary key."""
        return cls.query.get(user_id)

    @classmethod
    def get_by_email(cls, email):
        """Return a user by email."""
        return cls.query.filter_by(email=email).first()

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Movie(db.Model):
    """A movie."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    poster_path = db.Column(db.String, nullable=False)

    @classmethod
    def create(cls, title, overview, release_date, poster_path):
        """Create and return a new movie."""
        return cls(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    @classmethod
    def get_all(cls):
        """Return all movies."""
        return cls.query.all()

    @classmethod
    def get_by_id(cls, movie_id):
        """Return a movie by primary key."""
        return cls.query.get(movie_id)

    def __repr__(self):
        return f"<Movie movie_id={self.movie_id} title={self.title}>"

class Rating(db.Model):
    """A movie rating."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")

    @classmethod
    def create(cls, user, movie, score):
        """Create and return a new rating."""
        return cls(user=user, movie=movie, score=score)

    @classmethod
    def update(cls, rating_id, new_score):
        """Update a rating given rating_id and the updated score."""
        rating = cls.query.get(rating_id)
        if rating:
            rating.score = new_score
            db.session.commit()
        return rating

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    """Connect the database to our Flask app."""
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
