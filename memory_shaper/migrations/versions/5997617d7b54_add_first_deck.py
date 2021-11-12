"""Add first deck

Revision ID: 5997617d7b54
Revises: 250656cfacc9
Create Date: 2021-11-06 21:11:21.286540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5997617d7b54'
down_revision = '250656cfacc9'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO deck (name) values ('Eng - Rus initial deck')
        """
    )


def downgrade():
    pass
