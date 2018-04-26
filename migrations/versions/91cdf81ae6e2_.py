"""empty message

Revision ID: 91cdf81ae6e2
Revises: a8e4b9bbb442
Create Date: 2018-04-26 19:19:05.417007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '91cdf81ae6e2'
down_revision = 'a8e4b9bbb442'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project_disbursements', 'disb_status',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('projects', 'proj_approval',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)

    op.alter_column('users', 'disbursements_approval_rights',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    #op.alter_column('users', 'user_name',new_column_name="user_email", existing_type=sa.VARCHAR(length=30), nullable=False)
    op.add_column('users', sa.Column('user_name', sa.VARCHAR(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.alter_column('users', 'user_email',new_column_name="user_name", existing_type=sa.VARCHAR(length=30), nullable=False)
    op.alter_column('users', 'disbursements_approval_rights',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.drop_column('users', 'user_name')
    op.alter_column('projects', 'proj_approval',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('project_disbursements', 'disb_status',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###