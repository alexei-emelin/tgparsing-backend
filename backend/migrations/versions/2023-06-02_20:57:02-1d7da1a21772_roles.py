"""roles

Revision ID: 1d7da1a21772
Revises: 7059deaf392f
Create Date: 2023-06-02 20:57:02.573040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1d7da1a21772"
down_revision = "7059deaf392f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "roles",
        sa.Column(
            "name",
            sa.Enum("user", "admin", "accountant", name="roleschoice"),
            nullable=False,
        ),
        sa.Column("permissions", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("name"),
        sa.UniqueConstraint("name"),
    )
    op.add_column("users", sa.Column("is_staff", sa.Boolean(), nullable=False))
    op.add_column(
        "users",
        sa.Column(
            "role_name",
            sa.Enum("user", "admin", "accountant", name="roleschoice"),
            nullable=False,
        ),
    )
    op.create_foreign_key(
        "users_roles_name_fkey", "users", "roles", ["role_name"], ["name"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("users_roles_name_fkey", "users", type_="foreignkey")
    op.drop_column("users", "role_name")
    op.drop_column("users", "is_staff")
    op.drop_table("roles")
    op.execute("DROP TYPE roleschoice;")
    # ### end Alembic commands ###
