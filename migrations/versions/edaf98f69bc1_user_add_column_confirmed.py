"""user add column confirmed

Revision ID: edaf98f69bc1
Revises: d7fd99319024
Create Date: 2017-03-29 22:13:44.979788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edaf98f69bc1'
down_revision = 'd7fd99319024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venus_user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venus_user', 'confirmed')
    # ### end Alembic commands ###
