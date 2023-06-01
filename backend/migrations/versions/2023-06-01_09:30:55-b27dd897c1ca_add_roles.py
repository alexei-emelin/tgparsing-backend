"""add_roles

Revision ID: b27dd897c1ca
Revises: 7059deaf392f
Create Date: 2023-06-01 09:30:55.786977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b27dd897c1ca"
down_revision = "7059deaf392f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("permissions", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.add_column("users", sa.Column("role_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "users", "roles", ["role_id"], ["id"])

    op.bulk_insert(
        sa.Table(
            "roles",
            sa.MetaData(),
            sa.Column("name", sa.String()),
        ),
        [
            {"name": "User"},
            {"name": "PremiumUser"},
            {"name": "Admin"},
            {"name": "Manager"},
            {"name": "Accountant"},  # бухгалтер
            {"name": "Stakeholder"},
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="foreignkey")
    op.drop_column("users", "role_id")
    op.drop_table("roles")
    # ### end Alembic commands ###
