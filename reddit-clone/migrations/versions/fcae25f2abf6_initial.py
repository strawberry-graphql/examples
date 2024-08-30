"""initial

Revision ID: fcae25f2abf6
Revises:
Create Date: 2021-10-14 16:05:02.497467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fcae25f2abf6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("avatar", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "subreddits",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=75), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("icon", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=True),
        sa.Column("text", sa.String(length=1024), nullable=True),
        sa.Column("link", sa.String(length=255), nullable=True),
        sa.Column("thumbnail", sa.String(length=255), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("subreddit_id", sa.Integer(), nullable=True),
        sa.Column("votes", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["subreddit_id"],
            ["subreddits.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("link"),
    )
    op.create_table(
        "subreddit_users",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("subreddit_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["subreddit_id"],
            ["subreddits.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "subreddit_id"),
    )
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("votes", sa.Integer(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("post_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("comments")
    op.drop_table("subreddit_users")
    op.drop_table("posts")
    op.drop_table("subreddits")
    op.drop_table("users")
