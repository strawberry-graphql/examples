"""Add data

Revision ID: de9b93822f7c
Revises: 705aa75ea67b
Create Date: 2021-09-19 10:07:39.348634

"""
from alembic import op
from sqlalchemy import orm
from faker import Faker

from main.models import Person


# revision identifiers, used by Alembic.
revision = "de9b93822f7c"
down_revision = "705aa75ea67b"
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    fake = Faker()

    for i in range(1, 10001):
        person = Person(
            id=i,
            name=fake.name(),
        )
        session.add(person)
        session.commit()


def downgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    session.execute("DELETE FROM people")
    session.commit()
    session.close()
