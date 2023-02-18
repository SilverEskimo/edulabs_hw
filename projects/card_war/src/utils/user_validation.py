class UserValidation:
    @staticmethod
    def valid_coin_choice(coin_choice: str):
        if coin_choice.lower() not in ('h', 't'):
            raise Exception("Error: please choose 'h' for heads or 't' for tails")
    @staticmethod
    def valid_proceed(proceed: str):
        if proceed.lower() not in ("y", "n"):
            raise Exception("Error: please choose 'y' for yes or 'n' for no")
        return proceed.lower()