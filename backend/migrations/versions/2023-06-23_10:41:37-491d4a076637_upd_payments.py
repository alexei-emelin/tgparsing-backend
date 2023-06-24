"""upd payments

Revision ID: 491d4a076637
Revises: 9d0d330eaebf
Create Date: 2023-06-23 10:41:37.335800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "491d4a076637"
down_revision = "9d0d330eaebf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "payments", sa.Column("status", sa.Boolean(), nullable=False)
    )
    op.alter_column(
        "payments",
        "amount",
        existing_type=sa.INTEGER(),
        type_=sa.Numeric(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "payments",
        "amount",
        existing_type=sa.Numeric(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.drop_column("payments", "status")
    # ### end Alembic commands ###
