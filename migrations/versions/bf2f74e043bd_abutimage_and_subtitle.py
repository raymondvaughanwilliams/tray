"""abutimage and subtitle

Revision ID: bf2f74e043bd
Revises: c01f408e6da1
Create Date: 2021-12-07 20:33:16.611896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf2f74e043bd'
down_revision = 'c01f408e6da1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('about', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('about', sa.Column('image', sa.VARCHAR(length=64), nullable=False))
    # ### end Alembic commands ###