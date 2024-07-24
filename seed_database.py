"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

def reset_database():
    """Reset the database by dropping and creating it."""
    os.system("dropdb ratings")
    os.system("createdb ratings")

def load_movie_data(file_path):
    """Load movie data from JSON file."""
    with open(file_path) as f:
        return json.loads(f.read())

def seed_movies(movie_data):
    """Create movies and store them in the database."""
    movies_in_db = []
    for movie in movie_data:
        title = movie["title"]
        overview = movie["overview"]
        poster_path = movie["poster_path"]
        release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

        db_movie = crud.create_movie(title, overview, release_date, poster_path)
        movies_in_db.append(db_movie)

    model.db.session.add_all(movies_in_db)
    model.db.session.commit()
    return movies_in_db

def seed_users_and_ratings(movies_in_db):
    """Create users and ratings, and store them in the database."""
    for n in range(10):
        email = f"user{n}@test.com"
        password = "test"

        user = crud.create_user(email, password)
        model.db.session.add(user)

        for _ in range(10):
            random_movie = choice(movies_in_db)
            score = randint(1, 5)

            rating = crud.create_rating(user, random_movie, score)
            model.db.session.add(rating)

    model.db.session.commit()

if __name__ == "__main__":
    reset_database()
    model.connect_to_db(server.app)
    model.db.create_all()

    movie_data = load_movie_data("data/movies.json")
    movies_in_db = seed_movies(movie_data)
    seed_users_and_ratings(movies_in_db)
