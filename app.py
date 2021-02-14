from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '4b8z6b2x'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()
words = boggle_game.words

@app.route('/game-page')
def show_game_page():
    """Make the game board, set it in the session, and show the page."""
    game_board = make_board()
    set_board_in_session(game_board)
    
    return render_template('game-page.html', game_board = game_board)

@app.route('/submit-guess', methods=['POST'])
def handle_guess():
    """Check if the word that the user enters is valid or not. Then respond
    with an appropriate message.
    """
    user_guess = request.get_json()['guess']
    
    if check_if_real_word(user_guess) and check_if_on_board(user_guess):
        return jsonify({'result': 'ok'})
    elif check_if_real_word(user_guess) and not check_if_on_board(user_guess):
        return jsonify({'result': 'not-on-board'})
    else:
        return jsonify({'result': 'not-a-word'})

@app.route('/statistics', methods=['POST'])
def handle_stats():
    """Update the number of times that the user plays the game, get the score
    from the user, and check if it's the highest score.
    """
    update_num_of_plays_in_session()
    score = request.get_json()['score']
    if is_highest_score(score):
        set_highest_score_in_session(score)

    return 'Thanks for the statistics'

def make_board():
    """Make the game board and return it."""
    game_board = boggle_game.make_board()
    return game_board

def set_board_in_session(game_board):
    """Set the game board in the session."""
    session['game_board'] = game_board

def check_if_real_word(word):
    """Check if the user entered a word that's in the dictionary."""
    if word in words:
        return True
    return

def check_if_on_board(word):
    """Check if the word is on the board. Return True if so, False otherwise."""
    if boggle_game.check_valid_word(board = session['game_board'], word=word) == 'ok':
        return True
    elif boggle_game.check_valid_word(board = session['game_board'], word=word) == 'not-on-board':
        return False

def is_highest_score(score):
    """Check if the score the user got is greater than the highest score."""
    if score > session.get('highest_score', 0):
        return True

def set_highest_score_in_session(score):
    """Put the highest score into the session."""
    session['highest_score'] = score

def update_num_of_plays_in_session():
    """Update the number of times that the user played the game in the session."""
    num_of_plays = session.get('num_of_plays', 0)
    num_of_plays += 1
    session['num_of_plays'] = num_of_plays