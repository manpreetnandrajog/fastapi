"""auto-vote

Revision ID: b9e1d0b1254d
Revises: e5fed85147d9
Create Date: 2022-03-26 23:53:28.165334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9e1d0b1254d'
down_revision = 'e5fed85147d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('contents', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('published', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='post_users_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    # ### end Alembic commands ###
