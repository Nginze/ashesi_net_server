"""likes structure

Revision ID: 0557fe8106bb
Revises:
Create Date: 2023-04-15 16:30:21.624018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0557fe8106bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.alter_column('creator_id',
                              existing_type=sa.UUID(),
                              nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('likes', schema=None) as batch_op:
        batch_op.alter_column('creator_id',
                              existing_type=sa.UUID(),
                              nullable=False)

    # ### end Alembic commands ###
