"""rename date of birth to dob

Revision ID: bfc306cd8a41
Revises: 99d3953dd783
Create Date: 2023-10-16 16:14:22.999690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfc306cd8a41'
down_revision = '99d3953dd783'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
            RENAME COLUMN date_of_birth TO dob;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
            RENAME COLUMN dob TO date_of_birth;
        """
    )
