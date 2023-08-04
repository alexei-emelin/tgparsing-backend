"""change users and tasks

Revision ID: 0525ced27760
Revises: d6076d46d8a8
Create Date: 2023-08-03 22:07:12.977341

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0525ced27760'
down_revision = 'd6076d46d8a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               existing_nullable=False)
    # ### end Alembic commands ###
