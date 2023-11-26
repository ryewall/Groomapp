"""add customers date_of_birth

Revision ID: 1312f9136ee4
Revises: 3cccfd230db4
Create Date: 2023-10-16 15:48:50.518598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1312f9136ee4'
down_revision = '3cccfd230db4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )