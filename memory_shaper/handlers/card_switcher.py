from typing import List, Optional

from memory_shaper.algorithm.FlashCardAlgo import get_modified_card, FlashCardAlgorithm
from memory_shaper.tmp_cards import CARDS, init_queue, get_queue

from flask import render_template, redirect, url_for, request, session

from app import app
from memory_shaper.app import new_sql_session
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

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



@app.route('/card', methods=['GET'])
def card():
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

    user_card_id = session['current_user_card_id']
    sql_session = new_sql_session()
    user_card = (
        sql_session.query(models.UserCard).get(user_card_id)
    )  # type: models.UserCard

    algo_card = FlashCardAlgorithm(
        user_card.algo_data.setdefault('delta', 1),
        user_card.algo_data.setdefault('n_of_showings', 0),
        user_card.algo_data.setdefault('n_of_correct_ans', 0),
    )
    algo_card = get_modified_card(algo_card, request.form['button'] == 'Correct')

    user_card.next_show_date = algo_card.next_show
    user_card.algo_data['delta'] = algo_card.current_delta
    user_card.algo_data['n_of_showings'] = algo_card.number_of_showings
    user_card.algo_data['n_of_correct_ans'] = algo_card.number_of_correct_ans
    flag_modified(user_card, "algo_data")
    sql_session.flush()
    sql_session.commit()
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
