"""Added chat_id field, renamed chat name field

Revision ID: 213c83c48549
Revises: 196f435444ec
Create Date: 2023-07-09 17:07:21.003807

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '213c83c48549'
down_revision = '196f435444ec'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chats', sa.Column('chat_id', sa.BIGINT(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chats', 'chat_id')
    # ### end Alembic commands ###
