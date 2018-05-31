"""empty message

Revision ID: 67eda80b260f
Revises: e716ef7a7366
Create Date: 2018-05-31 23:26:16.185158

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '67eda80b260f'
down_revision = 'e716ef7a7366'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project_disbursements', 'disb_status',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.create_foreign_key(None, 'project_issues', 'projects', ['issue_proj'], ['proj_id'])
    op.alter_column('projects', 'proj_approval',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('users', 'disbursements_approval_rights',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('users', 'user_approver_rights',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('warehouse_users', 'user_approver_rights',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('warehouse_users', 'user_approver_rights',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('users', 'user_approver_rights',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('users', 'disbursements_approval_rights',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('projects', 'proj_approval',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_constraint(None, 'project_issues', type_='foreignkey')
    op.alter_column('project_disbursements', 'disb_status',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###