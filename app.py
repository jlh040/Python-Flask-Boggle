from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '4b8z6b2x'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/game-page')
def show_game_page():
    """Show the game board and put the board in the session"""
    game_board = boggle_game.make_board()
    session['game_board'] = game_board
    return render_template('game-page.html', game_board = game_board)