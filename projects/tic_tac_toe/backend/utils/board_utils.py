from projects.tic_tac_toe.frontend.utils.user_input_validation import user_move_validation


def check_if_taken(user_move: tuple, current_state: dict) -> tuple:
    """
    Check if the cell that was selected is already taken
    :param user_move: Current move's coordinates
    :param current_state: Current game's state
    :return:
    Returns a tuple with a valid move
    """
    row, col = user_move
    while True:
        if current_state["current_board"][int(row)-1][int(col)-1]:
            move_tuple = user_move_validation(input(f"This spot is taken. Please try again: ").strip(), current_state)
            row, col = move_tuple
        else:
            break
    return row, col


def update_current_player(current_state: dict):
    """
    Updates the current player in the current game state
    :param current_state:
    :return:
        Void
    """
    current_state["current_player"] = 0 if current_state["current_player"] == 0 else current_state["current_player"] = 1


def get_state_params(current_state: dict) -> tuple:
    """
    Get attributes of the current game state
    :param current_state:
    :return:
    Returns a tuple with the current board, current player, board size, and the current char
    """
    current_board = current_state.get("current_board")
    current_player = current_state.get("current_player")
    board_size = current_state.get("board_size")
    current_char = current_state.get("char")[current_player]
    return current_board, current_player, board_size, current_char


def check_win(current_state: dict, option_to_win) -> bool:
    """
    Checks if there's a winner in any possible option
    :param current_state: current game's state
    :param option_to_win: options for the win (row, col or diagonal)
    :return:
    True if there's a winner, else False
    """
    current_board, current_player, board_size, current_char = get_state_params(current_state)
    count = 0
    for i, row in enumerate(current_board):
        for j, col in enumerate(current_board):
            match option_to_win:
                case "row":
                    if not current_board[i][j]:
                        count == 0
                        break
                    elif current_board[i][j] == current_char and count != board_size:
                        count += 1
                    else:
                        count == 0
                case "col":
                    if not current_board[i][0]:
                        count == 0
                        break
                    elif current_board[i][0] == current_char and count != board_size:
                        count += 1
                        break
                    else:
                        count == 0
                case "diagonal":
                    if not current_board[i][i]:
                        count == 0
                        break
                    elif current_board[i][i] == current_char and count != board_size:
                        count += 1
                        break
                    elif current_board[i][-(i+1)] == current_char and count != board_size:
                        count += 1
                        break
                    else:
                        count == 0
    if count == board_size:
        return True
    return False


def map_cells(current_state: dict) -> None:
    if not current_state["cells_list"]:
        board_size = current_state.get("board_size")
        for i in range(board_size):
            for j in range(board_size):
                current_state["cells_list"].append((i, j))
