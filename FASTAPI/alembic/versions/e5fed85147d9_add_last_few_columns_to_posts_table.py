"""add last few columns to posts table

Revision ID: e5fed85147d9
Revises: 8f4e0c630401
Create Date: 2022-03-25 01:22:34.760375

"""
from datetime import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5fed85147d9'
down_revision = '8f4e0c630401'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
