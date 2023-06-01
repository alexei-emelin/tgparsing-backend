"""add avatar url field into users table

Revision ID: 7059deaf392f
Revises: 3ed9f7222040
Create Date: 2023-05-31 20:36:42.554621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7059deaf392f"
down_revision = "3ed9f7222040"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("avatar_url", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "avatar_url")
    # ### end Alembic commands ###
