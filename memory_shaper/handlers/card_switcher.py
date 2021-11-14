from memory_shaper.algorithm.FlashCardAlgo import get_modified_card
from memory_shaper.tmp_cards import CARDS, init_queue, get_queue

from flask import render_template, redirect, url_for, request, session

from app import app


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


@app.route('/check_answer', methods=['POST'])
def check_answer():
    queue = get_queue()
    next_time, i = queue.get()
    CARDS[i] = get_modified_card(CARDS[i], request.form['button'] == 'Correct')
    queue.put((CARDS[i].get_next_show_time(), i))
    return redirect(url_for('card'))
