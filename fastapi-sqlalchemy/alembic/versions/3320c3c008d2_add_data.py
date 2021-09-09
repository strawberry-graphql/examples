"""Add data

Revision ID: 3320c3c008d2
Revises: d117aba82184
Create Date: 2021-09-09 21:16:08.831902

"""
import json
from pathlib import Path

from alembic import op
from sqlalchemy import orm

from main.models import Director, Movie


# revision identifiers, used by Alembic.
revision = "3320c3c008d2"
down_revision = "d117aba82184"
branch_labels = None
depends_on = None

current_dir = Path(__file__).parent.resolve()
data_file = current_dir.parent.parent.parent / Path("common-data") / Path("movies.json")


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    with data_file.open() as f:
        json_data = json.load(f)

    for movie_data in json_data:
        director = (
            session.query(Director)
            .filter_by(name=movie_data["director"]["name"])
            .first()
        )
        if not director:
            director = Director(name=movie_data["director"]["name"])
            session.add(director)
            session.commit()

        movie = Movie(
            imdb_id=movie_data["imdb_id"],
            title=movie_data["title"],
            year=movie_data["year"],
            image_url=movie_data["image_url"],
            imdb_rating=movie_data["imdb_rating"],
            imdb_rating_count=movie_data["imdb_rating_count"],
            director=director,
        )
        session.add(movie)
        session.commit()


def downgrade():
    pass
