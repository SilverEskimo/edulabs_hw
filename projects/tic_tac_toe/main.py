from projects.tic_tac_toe.backend.board import *
from projects.tic_tac_toe.frontend.user_input import *
from projects.tic_tac_toe.frontend.utils.prints import *

if __name__ == '__main__':

    print_greeting()
    names = get_names()
    board_size = get_board_size()
    board = initialize_board(board_size)

    current_state = {
        "current_player": 0,
        "players_names": [names[0], names[1]],
        "current_board": board,
        "board_size": board_size,
        "char": ["X", "O"],
        "board_cells_list": [],
        "cells_list": [],
    }
    map_cells(current_state)
    print_good_luck(names, board_size)
    print_board(board_size, current_state, initiate=True)
    win = False
    while True:
        move = get_user_move(current_state)
        if move:
            win = player_move(move, current_state)
            if not win:
                update_current_player(current_state)
                print_board(board_size, current_state)
                if win is None:
                    print("\tThe game is stuck, please try again")
                    break
            else:
                print_winner(current_state)
                break



