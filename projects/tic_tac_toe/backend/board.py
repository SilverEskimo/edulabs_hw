from projects.tic_tac_toe.backend.utils.board_utils import *


def initialize_board(board_size: int) -> list[list[int]]:
    res_board = []
    for row in range(board_size):
        res_board.append([])
        for col in range(board_size):
            res_board[row].append([])
            for var in range(board_size):
                res_board[row][col] = None
    return res_board


def player_move(user_move: tuple, current_state: dict) -> bool:
    """
    A function to update user's move and check if the user has won
    :param user_move: current move's coordinates
    :param current_state: current game state
    :return:
        True if there's a winner, else False
    """
    options_to_win = ("row", "col", "diagonal")
    win = False
    row, col = user_move
    current_char = current_state.get("char")[current_state["current_player"]]
    current_state["current_board"][int(row) - 1][int(col) - 1] = current_char
    for option in options_to_win:
        if check_win(current_state, option):
            return True
    return False

