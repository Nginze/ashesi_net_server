"""Adding Extra fields User

Revision ID: 657a112ede0e
Revises: 0557fe8106bb
Create Date: 2023-04-22 01:25:59.100490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '657a112ede0e'
down_revision = '0557fe8106bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_food', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('favorite_movie', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('year_group', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('major', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('residency', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('date_of_birth', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('date_of_birth')
        batch_op.drop_column('residency')
        batch_op.drop_column('major')
        batch_op.drop_column('year_group')
        batch_op.drop_column('favorite_movie')
        batch_op.drop_column('favorite_food')

    # ### end Alembic commands ###
