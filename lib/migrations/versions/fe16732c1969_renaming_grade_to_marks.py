"""Renaming grade to marks

Revision ID: fe16732c1969
Revises: 791279dd0760
Create Date: 2024-07-16 12:26:14.056348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe16732c1969'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('grade', new_column_name='marks')


def downgrade() -> None:
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('marks', new_column_name='grade')

