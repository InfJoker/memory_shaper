from typing import List, Optional

from memory_shaper.algorithm.FlashCardAlgo import get_modified_card
from memory_shaper.tmp_cards import CARDS, init_queue, get_queue

from flask import render_template, redirect, url_for, request, session

from app import app
from memory_shaper.app import new_sql_session
from sqlalchemy.orm import Session

from memory_shaper import models


@app.route('/')
def init_session():
    init_queue()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['login'] or not request.form['password']:
            return redirect(url_for('login'))
        else:
            session['login'] = request.form['login']
            sql_session = new_sql_session()
            user = (
                sql_session.query(models.User).filter_by(login=session['login']).one_or_none()
            )  # type: Optional[models.User]

            session['user_nickname'] = user.nickname

            if user is None:
                return redirect(url_for('login'))

            update_user_decks(sql_session, user)
            return redirect(url_for('card'))
    return render_template('login.html')


@app.route('/card')
def card():
    if 'login' not in session:
        return redirect(url_for('login'))
    queue = get_queue()
    next_time, i = queue.get()
    queue.put((next_time, i))
    return render_template('flash_card.html', question=CARDS[i].question, answer=CARDS[i].answer)


@app.route('/card_base', methods=['GET'])
def card_base():
    if 'login' not in session:
        return redirect(url_for('login'))
    session['current_deck_id'] = 1
    sql_session = new_sql_session()
    user_card = (
        sql_session.query(models.UserCard).filter(models.UserCard.deck_id == session['current_deck_id']).order_by(models.UserCard.next_show_date).limit(1).one_or_none()
    )  # type: Optional[models.UserCard]
    card_ = user_card.card
    session['current_user_card_id'] = user_card.id
    return render_template('flash_card.html', question=card_.card_front, answer=card_.card_back)


@app.route('/check_answer', methods=['POST'])
def check_answer():
    queue = get_queue()
    next_time, i = queue.get()
    CARDS[i] = get_modified_card(CARDS[i], request.form['button'] == 'Correct')
    queue.put((CARDS[i].get_next_show_time(), i))
    return redirect(url_for('card'))


def update_user_decks(sql_session: Session, user: models.User) -> None:
    user_decks = (
        sql_session.query(models.UserDeck).filter_by(user_nickname=user.nickname).all()
    )  # type: List[models.UserDeck]
    for user_deck in user_decks:
        fill_user_deck(sql_session, user_deck)


def fill_user_deck(sql_session: Session, user_deck: models.UserDeck) -> int:
    user_cards = (
        sql_session.query(models.UserCard).filter_by(deck_id=user_deck.deck_id).all()
    )  # type: List[models.UserCard]
    cards_in_deck_ids = [user_card.card_id for user_card in user_cards]
    cards_to_fill = (
        sql_session.query(models.Card)
        .filter_by(deck_id=user_deck.deck_id)
        .filter(models.Card.id.not_in(cards_in_deck_ids))
        .all()
    )  # type: List[models.Card]
    for card in cards_to_fill:
        instance = models.UserCard(user=user_deck.user, deck_id=user_deck.deck_id, card=card)
        sql_session.add(instance)
    sql_session.commit()
    return len(cards_to_fill)
