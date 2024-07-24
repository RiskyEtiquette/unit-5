# """CRUD operations."""

# from model import db, User, Movie, Rating, connect_to_db

# def create_user(email, password):
#     """Create and return a new user."""
#     return User(email=email, password=password)

# def get_users():
#     """Return all users."""
#     return User.query.all()

# def get_user_by_id(user_id):
#     """Return a user by primary key."""
#     return User.query.get(user_id)

# def get_user_by_email(email):
#     """Return a user by email."""
#     return User.query.filter(User.email == email).first()

# def create_movie(title, overview, release_date, poster_path):
#     """Create and return a new movie."""
#     return Movie(
#         title=title,
#         overview=overview,
#         release_date=release_date,
#         poster_path=poster_path,
#     )

# def get_movies():
#     """Return all movies."""
#     return Movie.query.all()

# def get_movie_by_id(movie_id):
#     """Return a movie by primary key."""
#     return Movie.query.get(movie_id)

# def create_rating(user, movie, score):
#     """Create and return a new rating."""
#     return Rating(user=user, movie=movie, score=score)

# def update_rating(rating_id, new_score):
#     """Update a rating given rating_id and the updated score."""
#     rating = Rating.query.get(rating_id)
#     if rating:
#         rating.score = new_score
#         db.session.commit()
#     return rating

# if __name__ == "__main__":
#     from server import app
#     connect_to_db(app)
