"""empty message

Revision ID: 0b62fbdc595d
Revises: dcc7957f3337
Create Date: 2019-11-18 12:12:56.738261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b62fbdc595d'
down_revision = 'dcc7957f3337'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('conditional_posting', sa.String(length=10), server_default='disabled', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'conditional_posting')
    # ### end Alembic commands ###
