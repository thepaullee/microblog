"""asdf

Revision ID: 8d5ff9644b6a
Revises: e77a06fac030
Create Date: 2019-05-15 15:55:17.759396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d5ff9644b6a'
down_revision = 'e77a06fac030'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=128), nullable=True))

    # ### end Alembic commands ###
