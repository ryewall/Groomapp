"""set date of birth non-nullable

Revision ID: 1e6a37d41c66
Revises: 1312f9136ee4
Create Date: 2023-10-16 16:07:31.299907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6a37d41c66'
down_revision = '1312f9136ee4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth SET NOT NULL;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth DROP NOT NULL;
        """
    )
