from PIL import Image
from card_war.src.backend.api_connector import ApiConnector


class CardWar:
    def __init__(self, user_details: tuple):
        self._user_state_dict = {
            "user1": {
                "name": user_details[0],
                "coin": user_details[1],
                "total_round_wins": 0
            },
            "user2": {
                "name": user_details[2],
                "coin": user_details[3],
                "total_round_wins": 0
            }
        }
        self._api_connector = ApiConnector()

    card_mapping = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13,
        "ACE": 14
    }

    def _update_user_state(self, user_state: dict):
        self._user_state_dict = user_state

    def flip_coin(self):
        headers = {
            "X-RapidAPI-Key": "155c89d05dmshc71bb589c25847bp17e1c3jsn602c542367b4",
            "X-RapidAPI-Host": "coin-flip1.p.rapidapi.com"
        }
        url = "https://coin-flip1.p.rapidapi.com/headstails"
        print("Calling Flip Coin API: ")
        response = self._api_connector.get_call(url, headers=headers)
        if response.status_code < 400:
            return response.json()
        raise Exception(f"The flip coin API call failed with status code: {response.status_code}")

    def initiate_deck(self):
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        response = self._api_connector.get_call(url)
        if response.status_code == 200:
            return response.json()["deck_id"]
        raise Exception(f"Failed to create a new deck with status code: {response.status_code}")

    def update_current_player(self):
        if self._user_state_dict.get("current_player") == 1:
            self._user_state_dict["current_player"] = 2
        else:
            self._user_state_dict["current_player"] = 1

    def _get_current_user(self):
        if self.get_user_state().get("current_player") == 1:
            return "user1"
        return "user2"

    def pull_card(self, deck_id: str):
        user_state = self.get_user_state()
        current_user = self._get_current_user()
        url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1"
        response = self._api_connector.get_call(url)
        if response.status_code < 400:
            user_state.get(current_user)["current_card"] = {
                "code": response.json().get("cards")[0].get("code"),
                "value": response.json().get("cards")[0].get("value"),
                "suit": response.json().get("cards")[0].get("suit"),
                "image": response.json().get("cards")[0].get("image")
            }
            return user_state.get(current_user).get("name"), user_state.get(current_user).get("current_card")
        raise Exception(f"Failed to pull a card for {user_state.get(current_user).get('name').title()} "
                        f"with status code: {response.status_code}")

    def determine_round_winner(self):
        first_card = self.get_user_state().get("user1").get("current_card").get("value")
        second_card = self.get_user_state().get("user2").get("current_card").get("value")
        if self.card_mapping[first_card.upper()] > self.card_mapping[second_card.upper()]:
            self._user_state_dict.get("user1")["total_round_wins"] += 1
            return self._user_state_dict.get('user1').get('name').title()
        elif self.card_mapping[first_card.upper()] < self.card_mapping[second_card.upper()]:
            self._user_state_dict.get("user2")["total_round_wins"] += 1
            return self._user_state_dict.get('user2').get('name').title()
        return False

    def get_user_state(self):
        return self._user_state_dict

    def get_game_winner(self):
        user_state = self.get_user_state()
        user1_wins = user_state.get("user1").get("total_round_wins")
        user2_wins = user_state.get("user2").get("total_round_wins")
        if user1_wins > user2_wins:
            return user_state.get("user1").get("name")
        elif user2_wins > user1_wins:
            return user_state.get("user2").get("name")
        return False

    def present_image(self):
        user_state = self.get_user_state()
        current_user = self._get_current_user()
        image_url = user_state[current_user].get("current_card").get("image")
        response = self._api_connector.get_call(image_url)
        with open("image.png", "wb") as f:
            f.write(response.content)
        image = Image.open("image.png")
        image.show()

    def reset_state(self):
        self.get_user_state().get("user1")["total_round_wins"] = 0
        self.get_user_state().get("user2")["total_round_wins"] = 0

    def __str__(self):
        return str(self._user_state_dict)
