
def print_greeting():
    print_greeting_board()
    print("\t\t\t\tHello!\nWelcome to the Tic-Tac-Toe game by Slava!\n")


def print_greeting_board():
    board = '''
              1   2   3  
            ✝---✝---✝---✝
          1 | T | I | C |
            ✝---✝---✝---✝
          2 | T | A | C |
            ✝---✝---✝---✝
          3 | T | O | E |
            ✝---✝---✝---✝ 
    '''
    print(board)


def print_good_luck(names, board_size):
    print(f"\nGood luck {names[0].title()} and {names[1].title()}! Enjoy the game!\n")


def print_board(board_size, current_state: dict = False, initiate=False):
    count = 1
    for row in range(1, board_size*2 + 2):
        print("\t\t\t", end="")
        for col in range(1, board_size*4+2):
            if row == 1 or row % 2 != 0:
                if col == 1 or count == 4:
                    print("✝", end="")
                    count = 1
                else:
                    print("-", end="")
                    count += 1
            else:
                if col == 1 or count == 4:
                    print("|", end="")
                    count = 1
                else:
                    if initiate:
                        if count == 2:
                            current_state["board_cells_list"].append((row, col))
                        print(" ", end="")
                    elif count == 2:
                        mapped_index = current_state["cells_list"][(current_state["board_cells_list"].index((row, col)))]
                        if current_state["current_board"][mapped_index[0]][mapped_index[1]]:
                            print(current_state["current_board"][mapped_index[0]][mapped_index[1]], end="")
                        else:
                            print(" ", end="")
                    else:
                        print(" ", end="")
                    count += 1
        print()


def print_winner(current_state: dict):
    current_player = current_state.get("current_player")
    winner_name = current_state.get("players_names")[current_player]
    print_winner_pattern()
    print_board(current_state["board_size"], current_state)
    print(f"\t  Congratulations {winner_name.title()}. You won!")


def print_winner_pattern():
    pattern = '''
  $$       $$  $$                                          $$
  $$   $   $$                                              $$
  $$  $$$  $$  $$  $$$$$$$   $$$$$$$    $$$$$$    $$$$$$   $$
  $$ $$ $$ $$  $$  $$    $$  $$   $$   $$    $$  $$   $$   $$
  $$$$   $$$$  $$  $$    $$  $$    $$  $$$$$$$$  $$        $$
  $$$     $$$  $$  $$    $$  $$    $$  $$        $$          
  $$       $$  $$  $$    $$  $$    $$   $$$$$$$  $$        $$
'''
    print(pattern)