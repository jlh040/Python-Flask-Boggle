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
    """Show the game board and put the board in the session."""
    game_board = make_board()
    set_session(game_board)
    return render_template('game-page.html', game_board = game_board)

@app.route('/submit-guess', methods=['POST'])
def handle_guess():
    user_guess = request.get_json()['guess']
    
    if check_if_real_word(user_guess) and check_if_on_board(user_guess):
        return jsonify({'result': 'ok'})
    elif check_if_real_word(user_guess) and not check_if_on_board(user_guess):
        return jsonify({'result': 'not-on-board'})
    else:
        return jsonify({'result': 'not-a-word'})





def make_board():
    game_board = boggle_game.make_board()
    return game_board

def set_session(game_board):
    session['game_board'] = game_board

def check_if_real_word(word):
    if word in words:
        return True
    return

def check_if_on_board(word):
    if boggle_game.check_valid_word(board = session['game_board'], word=word) == 'ok':
        return True
    elif boggle_game.check_valid_word(board = session['game_board'], word=word) == 'not-on-board':
        return False