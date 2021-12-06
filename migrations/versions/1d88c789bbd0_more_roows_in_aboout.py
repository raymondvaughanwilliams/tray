"""more roows in aboout

Revision ID: 1d88c789bbd0
Revises: 380286f5581d
Create Date: 2021-12-04 21:59:01.446922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d88c789bbd0'
down_revision = '380286f5581d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('about', sa.Column('subtitle', sa.String(length=140), nullable=True))
    op.add_column('about', sa.Column('feature_subtitle', sa.String(length=140), nullable=True))
    op.add_column('about', sa.Column('feature_paragraph', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('about', 'feature_paragraph')
    op.drop_column('about', 'feature_subtitle')
    op.drop_column('about', 'subtitle')
    # ### end Alembic commands ###