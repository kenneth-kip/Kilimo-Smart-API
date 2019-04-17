"""empty message

Revision ID: 68a1658b7955
Revises: 
Create Date: 2019-03-19 10:37:37.015471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68a1658b7955'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Produce',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('type', sa.Enum('VEGETABLE', 'FRUIT', name='producetype'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Region',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Price',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('low_price', sa.Numeric(scale=2), nullable=False),
    sa.Column('high_price', sa.Numeric(scale=2), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('produce_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['produce_id'], ['Produce.id'], ),
    sa.ForeignKeyConstraint(['region_id'], ['Region.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Price')
    op.drop_table('Region')
    op.drop_table('Produce')
    # ### end Alembic commands ###
