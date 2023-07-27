"""new_tariff

Revision ID: 8ae1b15678cd
Revises: 9bbaf25b5c1c
Create Date: 2023-07-07 14:10:13.994798

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '8ae1b15678cd'
down_revision = '9bbaf25b5c1c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_subscribe',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('tariff_id', sa.Integer(), nullable=False),
                    sa.Column('tariff_options', sa.JSON(), nullable=False),
                    sa.Column('start_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['tariff_id'], ['tariffs.id'],
                                            name=op.f(
                                                'fk_user_subscribe_tariff_id_tariffs')),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'],
                                            name=op.f(
                                                'fk_user_subscribe_user_id_users')),
                    sa.PrimaryKeyConstraint('id',
                                            name=op.f('pk_user_subscribe')),
                    sa.UniqueConstraint('user_id',
                                        name=op.f('uq_user_subscribe_user_id'))
                    )
    op.drop_table('tariff_benefits')
    op.drop_table('benefits')
    op.add_column('tariffs', sa.Column('options', sa.JSON(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tariffs', 'options')
    op.create_table('benefits',
                    sa.Column('id', sa.INTEGER(), autoincrement=True,
                              nullable=False),
                    sa.Column('name', sa.VARCHAR(), autoincrement=False,
                              nullable=False),
                    sa.PrimaryKeyConstraint('id', name='pk_benefits'),
                    sa.UniqueConstraint('name', name='uq_benefits_name')
                    )
    op.create_table('tariff_benefits',
                    sa.Column('id', sa.INTEGER(), autoincrement=True,
                              nullable=False),
                    sa.Column('tariff_id', sa.INTEGER(), autoincrement=False,
                              nullable=False),
                    sa.Column('benefit_id', sa.INTEGER(), autoincrement=False,
                              nullable=False),
                    sa.ForeignKeyConstraint(['benefit_id'], ['benefits.id'],
                                            name='fk_tariff_benefits_benefit_id_benefits'),
                    sa.ForeignKeyConstraint(['tariff_id'], ['tariffs.id'],
                                            name='fk_tariff_benefits_tariff_id_tariffs'),
                    sa.PrimaryKeyConstraint('id', name='pk_tariff_benefits')
                    )
    op.drop_table('user_subscribe')
    # ### end Alembic commands ###
