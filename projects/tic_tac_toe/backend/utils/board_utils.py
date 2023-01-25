def update_current_player(current_state: dict):
    """
    Updates the current player in the current game state
    :param current_state:
    :return:
        None
    """
    current_state["current_player"] = 0 if current_state["current_player"] == 1 else 1


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


def check_win(current_state: dict) -> bool | None:
    """
    Checks if there's a winner in any possible option
    :param current_state: current game's state
    :return:
    True if there's a winner, else False (None in case of a stuck game)
    """
    diagonal = check_diagonal_win(current_state)
    row = check_row_win(current_state)
    col = check_col_win(current_state)
    if diagonal is None and row is None and col is None:
        return
    return diagonal or row or col


def check_row_win(current_state: dict) -> bool | None:
    """
    Check if there's a winner by row
    :param current_state: current game's state
    :return:
    True if there's a winner, else False (None in case of a stuck game)
    """
    current_board, _, board_size, current_char = get_state_params(current_state)
    count_stuck_rows = 0
    for i in range(1, board_size + 1):
        row_set = set(current_board[i - 1])
        if len(row_set) == 1 and current_char in row_set:
            return True
        elif len(row_set) > 1 and len({'X', 'O'}.intersection(row_set)) == 2:
            count_stuck_rows += 1
        if count_stuck_rows == board_size:
            return
    return False


def check_diagonal_win(current_state: dict) -> bool | None:
    """
    Check if there's a winner by one of the two possible diagonals
    :param current_state: current game's state
    :return:
    True if there's a winner, else False (None in case of a stuck game)
    """
    current_board, _, board_size, current_char = get_state_params(current_state)
    first_diagonal_set = set()
    second_diagonal_set = set()
    for i in range(1, board_size + 1):
        first_diagonal_set.add(current_board[i - 1][i - 1])
        second_diagonal_set.add(current_board[i - 1][-i])
    if (len(first_diagonal_set) == 1 and current_char in first_diagonal_set) or \
            (len(second_diagonal_set) == 1 and current_char in second_diagonal_set):
        return True
    elif len(first_diagonal_set) > 1 and len({'X', 'O'}.intersection(first_diagonal_set)) == 2 and \
            len(second_diagonal_set) > 1 and len({'X', 'O'}.intersection(second_diagonal_set)) == 2:
        return
    return False


def check_col_win(current_state: dict) -> bool | None:
    """
    Check if there's a winner by a column
    :param current_state: current game's state
    :return:
    True if there's a winner, else False (None in case of a stuck game)
    """
    current_board, _, board_size, current_char = get_state_params(current_state)
    count = 0
    count_stuck_cols = 0
    for i in range(1, board_size + 1):
        for j in range(1, board_size + 1):
            if current_board[j - 1][i - 1] == current_char:
                count += 1
            elif current_board[j - 1][i - 1] is not None and count >= 1:
                count_stuck_cols += 1
        if count_stuck_cols == board_size:
            return
        if count == board_size:
            return True
        count = 0
    return False


def map_cells(current_state: dict) -> None:
    """
    Create a list of all existing cells in the board
    :param current_state: current game's state
    :return:
    None
    """
    if not current_state["cells_list"]:
        board_size = current_state.get("board_size")
        for i in range(board_size):
            for j in range(board_size):
                current_state["cells_list"].append((i, j))
