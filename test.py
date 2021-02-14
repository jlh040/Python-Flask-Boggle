from unittest import TestCase
from app import app, make_board, check_if_real_word, check_if_on_board, is_highest_score, set_highest_score_in_session, update_num_of_plays_in_session, set_board_in_session
from flask import session, jsonify, request
from boggle import Boggle
from random import choice
import flask

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

boggle_game = Boggle()


class FlaskTests(TestCase):
    def test_show_game_page(self):
        with app.test_client() as client:
            resp = client.get('/game-page')
            html = resp.get_data(as_text=True)

            self.assertIn('<h1>Boggle Game!</h1>', html)
            self.assertEqual(resp.status_code, 200)

    def test_handle_guess(self):
        # May fail sometimes due to the letters on the board being random
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['game_board'] = Boggle().make_board()
            resp = client.post('/submit-guess', json = {'guess': 'butter'})
            data = resp.get_json()
            self.assertEqual(data['result'], 'not-on-board')
            self.assertEqual(resp.status_code, 200)

            resp = client.post('/submit-guess', json = {'guess': 'a3424njndsjf323'})
            data = resp.get_json()
            self.assertEqual(data['result'], 'not-a-word')
            self.assertEqual(resp.status_code, 200)


            resp = client.post('/submit-guess', json = {'guess': 'b'})
            data = resp.get_json()
            self.assertEqual(data['result'], 'ok')
            self.assertEqual(resp.status_code, 200)

    
    def test_handle_stats(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['game_board'] = Boggle().make_board()
            resp = client.post('/statistics', json={'score': 5})
            data = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertTrue(data == 'Thanks for the statistics')

    def test_make_board(self):
        board = make_board()

        self.assertEqual(len(board), 5)
        self.assertTrue(board[0] and board[1] and board[2] and board[3] and board[4])

    def test_set_board_in_session(self):
        with app.test_request_context('/game-page'):
            game_board = Boggle().make_board()
            set_board_in_session(game_board)

            self.assertEqual(session['game_board'], game_board)


    def test_check_if_real_word(self):
        word = choice(Boggle().words)
        
        self.assertFalse(check_if_real_word('jjfdsoijvoivoioidijfsoi'))
        self.assertTrue(check_if_real_word('Jeffrey'))

    def test_check_if_on_board(self):
        # May fail sometimes due to the letters on the board being random
        with app.test_request_context('/game-page', json={'guess': 'something'}):
            session['game_board'] = Boggle().make_board()
            self.assertFalse(check_if_on_board('dsffsdf'))
            self.assertTrue(check_if_on_board('a'))

    def test_is_highest_score(self):
        with app.test_request_context('/statistics', json={'score': 15}):
            session['highest_score'] = 3
            self.assertTrue(is_highest_score(55))
            self.assertTrue(is_highest_score(4))

    def test_set_highest_score_in_session(self):
        with app.test_request_context('/statistics', json={'score': 43}):
            set_highest_score_in_session(43)
            self.assertEqual(session['highest_score'], 43)
    
    def test_update_num_plays_in_session(self):
        with app.test_request_context('/statistics', json={'score': 11}):
            session['num_of_plays'] = 4
            update_num_of_plays_in_session()

            self.assertEqual(session['num_of_plays'], 5)