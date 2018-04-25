"""empty message

Revision ID: e46735de6ef1
Revises: ede03d07e762
Create Date: 2018-04-25 17:05:37.239563

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e46735de6ef1'
down_revision = 'ede03d07e762'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_disbursements', sa.Column('disb_status', sa.Boolean(), nullable=True))
    op.drop_column('project_disbursements', 'disbt_status')
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.add_column('project_disbursements', sa.Column('disbt_status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('project_disbursements', 'disb_status')
    # ### end Alembic commands ###