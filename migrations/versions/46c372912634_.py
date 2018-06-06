"""empty message

Revision ID: 46c372912634
Revises: a7391b976b8b
Create Date: 2018-06-06 11:00:11.848840

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '46c372912634'
down_revision = 'a7391b976b8b'
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
    op.alter_column('users', 'user_approver_rights',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    #op.add_column('warehouse_products', sa.Column('product_units', sa.Integer(), nullable=False))
    op.alter_column('warehouse_products', 'product_type',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.Integer(),
               existing_nullable=False)
    op.create_foreign_key(None, 'warehouse_products', 'warehouse_categories', ['product_type'], ['cat_id'])
    op.create_foreign_key(None, 'warehouse_products', 'warehouse_units', ['product_units'], ['units_id'])
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
    op.drop_constraint(None, 'warehouse_products', type_='foreignkey')
    op.drop_constraint(None, 'warehouse_products', type_='foreignkey')
    op.alter_column('warehouse_products', 'product_type',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=False)
    op.drop_column('warehouse_products', 'product_units')
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
    op.alter_column('project_disbursements', 'disb_status',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###
