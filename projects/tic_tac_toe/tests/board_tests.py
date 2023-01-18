from pprint import pprint
from projects.tic_tac_toe.frontend.utils.prints import print_board
from projects.tic_tac_toe.backend.utils.board_utils import *


if __name__ == '__main__':
    current_state = {
        "current_player": 0,
        "players_names": ["test1", "test2"],
        "current_board": None,
        "board_size": 3,
        "char": ["O"],
        "board_cells_list": [ ],
        "cells_list": [ ],
    }


    def test_winner_row():
        board = [
            [None, None, None],
            ['O', 'O', 'O'],
            [None, None, None]
        ]
        current_state["current_board"] = board
        res = check_win(current_state)
        assert res is True, "Row winner test failed"

    def test_winner_col():
        board = [
            [None, 'O', None],
            ['O', 'O', None],
            [None, 'O', None]
        ]
        current_state["current_board"] = board
        res = check_win(current_state)
        assert res is True, "Col winner test failed"


    def test_winner_diagonal1():
        board = [
            [None, 'O', 'O'],
            ['X', 'O', None],
            ['O', None, None]
        ]
        current_state["current_board"] = board
        res = check_win(current_state)
        assert res is True, "Diagonal 1 winner test failed"


    def test_winner_diagonal2():
        board = [
            ['O', 'O', None],
            ['X', 'O', None],
            ['O', None, 'O']
        ]
        current_state["current_board"] = board
        res = check_win(current_state)
        assert res is True, "Diagonal 2 winner test failed"

    test_winner_row()
    test_winner_col()
    test_winner_diagonal1()
    test_winner_diagonal2()