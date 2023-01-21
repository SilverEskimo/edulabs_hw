from frontend.utils.user_input_validation import *


def get_names() -> tuple:
    msg = "Please enter the name of the players separated by space: "
    names = input(msg).strip()
    names_tuple = names_validation(names)
    while not names_tuple:
        names_tuple = names_validation(input(f"Wrong input! {msg}").strip())
    return names_tuple


def get_board_size():
    msg = "Please enter the board size (for example: 3 for 3x3) minimum 3 and up to 9"
    size = input(f"{msg}: ").strip()
    is_valid = board_size_validation(size)
    while not is_valid:
        size = input(f"Wrong input, {msg}: ")
        is_valid = board_size_validation(size)
    return int(size)


def get_user_move(current_state: dict, taken=False):
    player_num = current_state.get('current_player')
    player_name = current_state.get("players_names")[player_num]
    msg = f"It is {player_name}'s move. Please choose a valid row " \
          f"and column (separated by space): "
    move = input(msg).strip()
    move_tuple = user_move_validation(move, current_state)
    if move_tuple:
        move_tuple = check_if_taken(move_tuple, current_state)
    else:
        while not move_tuple:
            move_tuple = user_move_validation(input(f"Wrong input. {msg}").strip(), current_state)
    return move_tuple


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
            move_tuple = input(f"This spot is taken. Please try again: ").strip().split()
            row, col = move_tuple
        else:
            break
    return row, col


