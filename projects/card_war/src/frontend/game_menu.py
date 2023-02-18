from card_war.src.utils.user_validation import UserValidation


class GameMenu:
    @staticmethod
    def start_game_menu():
        coin_mapping = {
            "h": "Heads",
            "t": "Tails"
        }
        print("Welcome to Card War game!")
        first_user_name = input("Please enter 1st user name: ").strip()
        second_user_name = input("Please enter 2nd user name: ").strip()
        while True:
            try:
                first_user_choice = input(f"{first_user_name.title()} - please choose Heads or Tails (h/t): ")
                UserValidation.valid_coin_choice(first_user_choice)
                if first_user_choice == "h":
                    second_user_choice = "t"
                else:
                    second_user_choice = "h"
                break
            except Exception as e:
                print(f"\n{e}\n")
        return first_user_name, coin_mapping.get(first_user_choice.lower()), \
            second_user_name, coin_mapping.get(second_user_choice.lower())
    @staticmethod
    def next_round(round_count):
        while True:
            try:
                proceed = input(f"Shall we proceed to the next round? ({round_count + 1}/5, y/n): ")
                valid_proceed = UserValidation.valid_proceed(proceed)
                if valid_proceed == "y":
                    return True
                return False
            except Exception as e:
                print(f"\n{e}\n")
    @staticmethod
    def declare_winner(winner_name: str):
        print(f"Congratulations {winner_name.title()}, you won!")
