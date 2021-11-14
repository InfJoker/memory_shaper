"""Add french deck

Revision ID: bdd1e1c8eed8
Revises: 59861866d140
Create Date: 2021-11-14 22:31:22.145494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdd1e1c8eed8'
down_revision = '59861866d140'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO deck (name) values ('Easy French - Rus deck')
        """
    )
    op.execute(
        """
        INSERT INTO user_deck (user_nickname, deck_id) values ('Student', 2)
        """
    )


def downgrade():
    pass
