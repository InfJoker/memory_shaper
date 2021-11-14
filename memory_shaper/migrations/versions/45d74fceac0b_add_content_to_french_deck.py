"""Add content to french deck

Revision ID: 45d74fceac0b
Revises: bdd1e1c8eed8
Create Date: 2021-11-14 22:31:40.887597

"""
import csv

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45d74fceac0b'
down_revision = 'bdd1e1c8eed8'
branch_labels = None
depends_on = None


def upgrade():
    with open('parser/french_rus.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            query = (
                "INSERT INTO card (deck_id, card_front, card_back) values (2, E'{card_front}', '{card_back}')"
                .format(card_front=row['french'].replace("'", "''"), card_back=row['russian'])
            )
            op.execute(query)


def downgrade():
    pass
