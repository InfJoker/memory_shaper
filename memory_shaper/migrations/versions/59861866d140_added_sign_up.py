"""Added Sign Up

Revision ID: 59861866d140
Revises: f03b4c9273e6
Create Date: 2021-11-14 20:10:05.705962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59861866d140'
down_revision = 'f03b4c9273e6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        UPDATE auth_user 
        SET password='264c8c381bf16c982a4e59b0dd4c6f7808c51a05f64c35db42cc78a2a72875bb'
        WHERE login='student';
        """
    )


def downgrade():
    pass
