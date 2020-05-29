"""empty message

Revision ID: 260455e5c7d0
Revises: 
Create Date: 2020-05-28 22:51:02.700035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '260455e5c7d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('nickname', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('permLevel', sa.Integer(), nullable=False),
    sa.Column('signUpTime', sa.DateTime(), nullable=False),
    sa.Column('lastLoginTime', sa.DateTime(), nullable=False),
    sa.Column('icon', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('username'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('announce',
    sa.Column('announce_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('announce_id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('problem',
    sa.Column('problem_id', sa.Integer(), nullable=False),
    sa.Column('problemName', sa.String(length=100), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('info', sa.JSON(), nullable=False),
    sa.Column('build_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('problem_id'),
    sa.UniqueConstraint('problem_id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('tag',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('tag_name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('tag_id'),
    sa.UniqueConstraint('tag_name'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('relations',
    sa.Column('problem', sa.Integer(), nullable=True),
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problem'], ['problem.problem_id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tag.tag_id'], )
    )
    op.create_table('submission',
    sa.Column('submit_id', sa.Integer(), nullable=False),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('result', sa.String(length=10), nullable=False),
    sa.Column('result_msg', sa.Text(), nullable=True),
    sa.Column('resTime', sa.Float(), nullable=False),
    sa.Column('resMem', sa.Float(), nullable=False),
    sa.Column('code', sa.Text(), nullable=False),
    sa.Column('lang', sa.String(length=10), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.uid'], ),
    sa.ForeignKeyConstraint(['problem_id'], ['problem.problem_id'], ),
    sa.PrimaryKeyConstraint('submit_id'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission')
    op.drop_table('relations')
    op.drop_table('tag')
    op.drop_table('problem')
    op.drop_table('announce')
    op.drop_table('account')
    # ### end Alembic commands ###