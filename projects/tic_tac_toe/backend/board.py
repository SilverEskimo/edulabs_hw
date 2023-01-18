from projects.tic_tac_toe.backend.utils.board_utils import *


def initialize_board(board_size: int) -> list[list[int]]:
    """
    Initialize a new board
    :param board_size: board size provided by the user
    :return:
    list of lists - new initialized board
    """
    res_board = []
    for row in range(board_size):
        res_board.append([])
        for col in range(board_size):
            res_board[row].append([])
            for var in range(board_size):
                res_board[row][col] = None
    return res_board


def player_move(user_move: tuple, current_state: dict) -> bool | None:
    """
    A function to update user's move and check if the user has won
    :param user_move: current move's coordinates
    :param current_state: current game state
    :return:
        True if there's a winner, else False
    """
    row, col = user_move
    current_char = current_state.get("char")[current_state["current_player"]]
    current_state["current_board"][int(row) - 1][int(col) - 1] = current_char
    win = check_win(current_state)
    if not win:
        if win is None:
            return
        return False
    return True

