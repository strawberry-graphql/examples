"""Add person model

Revision ID: 705aa75ea67b
Revises: bea5e58f3328
Create Date: 2021-09-19 10:07:23.177957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "705aa75ea67b"
down_revision = "bea5e58f3328"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "people",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_people_id"), "people", ["id"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_people_id"), table_name="people")
    op.drop_table("people")
