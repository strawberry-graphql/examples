"""Add data

Revision ID: bea5e58f3328
Revises: 9bc8667ab6a6
Create Date: 2021-09-10 16:00:20.280277

"""
import json
from pathlib import Path

from alembic import op
from sqlalchemy import orm, select
from sqlalchemy.exc import NoResultFound

from main.models import Director, Movie


# revision identifiers, used by Alembic.
revision = "bea5e58f3328"
down_revision = "9bc8667ab6a6"
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
        try:
            director = session.execute(
                select(Director).filter_by(name=movie_data["director"]["name"])
            ).scalar_one()
        except NoResultFound:
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
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    session.execute("DELETE FROM movies")
    session.execute("DELETE FROM directors")
    session.commit()
    session.close()
