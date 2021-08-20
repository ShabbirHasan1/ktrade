"""Update table names

Revision ID: e9610f6e891c
Revises: 534e35784f6b
Create Date: 2021-08-20 09:45:24.509876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9610f6e891c'
down_revision = '534e35784f6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('configurations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key')
    )
    op.create_table('watched_tickers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticket')
    )
    op.drop_table('configuration')
    op.drop_table('watched_ticker')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watched_ticker',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ticket', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticket')
    )
    op.create_table('configuration',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('key', sa.VARCHAR(), nullable=False),
    sa.Column('value', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key')
    )
    op.drop_table('watched_tickers')
    op.drop_table('configurations')
    # ### end Alembic commands ###