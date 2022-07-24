"""add contents column to posts table

Revision ID: 4c3aae2ccfd6
Revises: e6c85c9f9da7
Create Date: 2022-03-25 00:32:54.264920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c3aae2ccfd6'
down_revision = 'e6c85c9f9da7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('contents', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'contents')
    pass
