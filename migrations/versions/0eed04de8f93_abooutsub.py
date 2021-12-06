"""abooutsub

Revision ID: 0eed04de8f93
Revises: d69e1b3e5910
Create Date: 2021-12-04 16:18:06.709812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eed04de8f93'
down_revision = 'd69e1b3e5910'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('about', sa.Column('about_subtitle', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('about', 'about_subtitle')
    # ### end Alembic commands ###