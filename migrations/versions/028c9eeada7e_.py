"""empty message

Revision ID: 028c9eeada7e
Revises: 
Create Date: 2022-08-03 11:45:43.308529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028c9eeada7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activities', 'description')
    # ### end Alembic commands ###
