from card_war.src.backend.card_war import CardWar
from card_war.src.frontend.game_menu import GameMenu


if __name__ == '__main__':
    menu = GameMenu()
    users_data = menu.start_game_menu()
    card_war = CardWar(users_data)
    count = 1
    try:
        flip_res = card_war.flip_coin()["outcome"]
        print("Flip result:", flip_res)
        user_state = card_war.get_user_state()
        if flip_res == user_state.get("user1").get("coin"):
            print(f"{user_state.get('user1').get('name')} pulls a card first")
            user_state["current_player"] = 1
        else:
            print(f"{user_state.get('user2').get('name')} pulls a card first")
            user_state["current_player"] = 2
        deck = card_war.initiate_deck()
        while count <= 5:
            first_user_card = card_war.pull_card(deck)
            print(f"{first_user_card[0].title()}'s card is:\n{first_user_card[1]['value']} of "
                  f"{first_user_card[1]['suit'].title()}")
            card_war.present_image()
            card_war.update_current_player()
            second_user_card = card_war.pull_card(deck)
            print(f"{second_user_card[0].title()}'s card is:\n{second_user_card[1]['value']} of "
                  f"{second_user_card[1]['suit'].title()}")
            card_war.present_image()
            card_war.determine_round_winner()
            card_war.update_current_player()
            if count <= 5:
                if count != 5:
                    next_round = menu.next_round(count)
                if not next_round or count == 5:
                    winner = card_war.get_game_winner()
                    if not winner:
                        print("It's a tie! Great job both!")
                        break
                    menu.declare_winner(winner)
                    break
            count += 1
    except Exception as e:
        print(f"\n{e}\n")


