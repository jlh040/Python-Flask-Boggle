from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '4b8z6b2x'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/game-page')
def show_game_page():
    """Show the game board and put the board in the session."""
    game_board = make_board()
    set_session(game_board)
    return render_template('game-page.html', game_board = game_board)

@app.route('/submit-guess', methods=['POST'])
def handle_guess():
    print(request.get_json()['guess'])
    info = {'name': 'diesel'}
    return jsonify(info)
    # print(request.form['guess'])




def make_board():
    game_board = boggle_game.make_board()
    return game_board

def set_session(game_board):
    session['game_board'] = game_board