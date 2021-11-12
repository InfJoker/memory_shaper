"""Add initial user with deck

Revision ID: 4e40f73baba1
Revises: 57dd876fcb22
Create Date: 2021-11-07 23:02:58.920973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e40f73baba1'
down_revision = '9750b6304ebe'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO auth_user (login, password, salt) values ('student', 'student', '')
        """
    )
    op.execute(
        """
        INSERT INTO "user" (login, nickname) values ('student', 'Student')
        """
    )
    op.execute(
        """
        INSERT INTO user_deck (user_nickname, deck_id) values ('Student', 1)
        """
    )


def downgrade():
    pass
