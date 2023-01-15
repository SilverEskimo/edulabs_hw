def board_size_validation(user_input: str) -> bool:
    if not user_input.isdigit():
        return False
    if int(user_input) < 3:
        return False
    return True


def names_validation(names: str) -> tuple | None:
    names_tuple = tuple(names.split(" "))
    if len(names_tuple) != 2:
        return
    return names_tuple


# Check the validity of each move made by the user:
def user_move_validation(move: str, current_state: dict) -> tuple | None:
    move_tuple = tuple(move.split(" "))
    if len(move_tuple) != 2:
        return
    row, col = move_tuple
    if not row.isdigit() or not col.isdigit():
        return
    if int(row) > current_state["board_size"] or int(col) > current_state["board_size"]:
        return
    return move_tuple


