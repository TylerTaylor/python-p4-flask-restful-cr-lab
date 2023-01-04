"""Create model Plant

Revision ID: 61b2afa6db18
Revises: 
Create Date: 2023-01-04 16:00:40.748688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b2afa6db18'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
