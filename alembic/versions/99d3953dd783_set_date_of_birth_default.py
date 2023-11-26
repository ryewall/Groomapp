"""set date of birth default

Revision ID: 99d3953dd783
Revises: 1e6a37d41c66
Create Date: 2023-10-16 16:11:17.471826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d3953dd783'
down_revision = '1e6a37d41c66'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth SET DEFAULT now();
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
            ALTER COLUMN date_of_birth DROP DEFAULT;
        """
    )
