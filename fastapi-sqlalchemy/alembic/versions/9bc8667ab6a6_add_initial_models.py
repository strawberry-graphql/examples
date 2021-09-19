"""Add initial models

Revision ID: 9bc8667ab6a6
Revises:
Create Date: 2021-09-10 16:00:02.842263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9bc8667ab6a6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "directors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_directors_id"), "directors", ["id"], unique=False)
    op.create_index(op.f("ix_directors_name"), "directors", ["name"], unique=True)
    op.create_table(
        "movies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("imdb_id", sa.String(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("image_url", sa.String(), nullable=False),
        sa.Column("imdb_rating", sa.Float(), nullable=False),
        sa.Column("imdb_rating_count", sa.String(), nullable=False),
        sa.Column("director_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["director_id"],
            ["directors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_index(op.f("ix_movies_id"), "movies", ["id"], unique=False)
    op.create_index(op.f("ix_movies_imdb_id"), "movies", ["imdb_id"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_movies_imdb_id"), table_name="movies")
    op.drop_index(op.f("ix_movies_id"), table_name="movies")
    op.drop_table("movies")
    op.drop_index(op.f("ix_directors_name"), table_name="directors")
    op.drop_index(op.f("ix_directors_id"), table_name="directors")
    op.drop_table("directors")
