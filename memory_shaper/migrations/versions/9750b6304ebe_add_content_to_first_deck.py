"""Add content to first deck

Revision ID: 9750b6304ebe
Revises: 5997617d7b54
Create Date: 2021-11-06 21:43:19.267100

"""
import csv

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9750b6304ebe'
down_revision = '5997617d7b54'
branch_labels = None
depends_on = None


def upgrade():
    with open('parser/eng_rus.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            query = (
                "INSERT INTO card (deck_id, card_front, card_back) values (1, '{card_front}', '{card_back}')"
                .format(card_front=row['english'], card_back=row['russian'])
            )
            op.execute(query)


def downgrade():
    pass
