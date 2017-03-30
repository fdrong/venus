"""first init

Revision ID: b494474e0090
Revises: 
Create Date: 2017-03-25 23:51:59.720558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b494474e0090'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venus_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('code', sa.String(length=500), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('telno', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_venus_company_name'), 'venus_company', ['name'], unique=True)
    op.create_table('venus_exam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('paper_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('type', sa.String(length=200), nullable=True),
    sa.Column('overdue', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('codename', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.String(length=200), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_role_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['venus_permission.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['venus_role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('mobilephone', sa.String(length=20), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Integer(), nullable=False),
    sa.Column('last_login_time', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['venus_company.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_venus_user_username'), 'venus_user', ['username'], unique=True)
    op.create_table('venus_exam_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('begin_at', sa.DateTime(), nullable=True),
    sa.Column('commit_at', sa.DateTime(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['exam_id'], ['venus_exam.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['venus_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=200), nullable=False),
    sa.Column('ip', sa.String(length=2000), nullable=True),
    sa.Column('message', sa.String(length=200), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['venus_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venus_user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['venus_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['venus_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venus_user_role')
    op.drop_table('venus_log')
    op.drop_table('venus_exam_user')
    op.drop_index(op.f('ix_venus_user_username'), table_name='venus_user')
    op.drop_table('venus_user')
    op.drop_table('venus_role_permission')
    op.drop_table('venus_role')
    op.drop_table('venus_permission')
    op.drop_table('venus_paper')
    op.drop_table('venus_exam')
    op.drop_index(op.f('ix_venus_company_name'), table_name='venus_company')
    op.drop_table('venus_company')
    # ### end Alembic commands ###
