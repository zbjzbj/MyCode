"""empty message

Revision ID: b4354dbc9b75
Revises: 42088f0246e2
Create Date: 2019-01-03 17:23:10.149888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4354dbc9b75'
down_revision = '42088f0246e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'price')
    # ### end Alembic commands ###
