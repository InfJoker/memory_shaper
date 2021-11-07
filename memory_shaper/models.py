from sqlalchemy import ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship

from app import db
from sqlalchemy.dialects.postgresql import JSON


class AuthUser(db.Model):
    __tablename__ = 'auth_user'

    login = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(65), nullable=False)
    salt = db.Column(db.String(80), nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    login = db.Column(ForeignKey('auth_user.login', ondelete='CASCADE'), nullable=False)
    nickname = db.Column(db.String(80), primary_key=True)
    first_name = db.Column(db.String(80))
    second_name = db.Column(db.String(80))

    auth_user = relationship(AuthUser, backref='user')


class Deck(db.Model):
    __tablename__ = 'deck'

    id = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(80))
    thematic = db.Column(db.String(80))
    description = db.Column(db.String)


class Card(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.INT, primary_key=True)
    deck_id = db.Column(ForeignKey('deck.id', ondelete='CASCADE'))
    card_front = db.Column(db.String(200))
    card_back = db.Column(db.String(200))

    deck = relationship(Deck)


class UserDeck(db.Model):
    __tablename__ = 'user_deck'

    id = db.Column(db.INT, primary_key=True)
    user_nickname = db.Column(ForeignKey('user.nickname', ondelete='CASCADE'))
    deck_id = db.Column(ForeignKey('deck.id', ondelete='CASCADE'))

    user = relationship(User)
    deck = relationship(Deck)


class UserCard(db.Model):
    __tablename__ = 'user_card'

    id = db.Column(db.INT, primary_key=True)
    user_nickname = db.Column(ForeignKey('user.nickname', ondelete='CASCADE'))
    card_id = db.Column(ForeignKey('card.id', ondelete='CASCADE'))
    next_show_date = db.Column(DateTime, nullable=False, default=sql.func.current_date())
    algo_data = db.Column(JSON, default=dict)

    card = relationship(Card)
    user = relationship(User)

