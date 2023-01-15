# transactions data - which action was performed when. transaction is an action performed
# on your account - deposit, withdrawal, conversion. For each transaction you should store the following:
# the date of the transaction (string in format dd-mm-yyyy)
# transaction type (deposit / withdrawal / conversion)
# amount
# currency
from datetime import date


class BankAccount:
    def __init__(
            self,
            account_number: int,
            account_holder: dict,
            maximum_credit: float,
            allowed_usd=False
    ):
        self.__account_number = account_number
        self.__account_holder = {
            "passport_num": account_holder["passport_num"],
            "name": account_holder["name"],
            "address": account_holder["address"],
            "phone": account_holder["phone"]
        }
        self.__allowed_usd = allowed_usd
        self.__shekel_balance = 0
        self.__usd_balance = 0 if self.__allowed_usd else None
        self.__maximum_credit = maximum_credit
        self.__transaction_data = {}
    rate = 3.42

    @staticmethod
    def _create_tx_log(operation_type: str, currency: str, amount: float) -> dict:
        return {
            "date": str(date.today()),
            "type": operation_type,
            "currency": currency,
            "amount": amount
        }

    def _add_transaction(self, transaction_details: dict) -> bool:
        tx_date = transaction_details["date"]
        if not self.__transaction_data.get(tx_date):
            self.__transaction_data[tx_date] = {}
            self.__transaction_data[tx_date] = [transaction_details]
            return True
        self.__transaction_data[tx_date].append(transaction_details)
        return True

    def deposit(self, amount_to_deposit: float, currency: str) -> bool:
        if currency.lower() == "usd":
            if not self.__allowed_usd:
                return False
            else:
                self.__usd_balance += amount_to_deposit
        else:
            self.__shekel_balance += amount_to_deposit
        self._add_transaction(self._create_tx_log("deposit", currency, amount_to_deposit))
        return True

    def withdraw(self, amount_to_withdraw: float, currency: str) -> bool:
        if currency.lower() == "usd":
            if self.__allowed_usd and self.__usd_balance - amount_to_withdraw >= 0:
                self.__usd_balance -= amount_to_withdraw
            else:
                return False
        else:
            if (self.__shekel_balance - amount_to_withdraw)*-1 <= self.__maximum_credit:
                self.__shekel_balance -= amount_to_withdraw
            else:
                return False
        self._add_transaction(self._create_tx_log("withdraw", currency, amount_to_withdraw))
        return True

    def convert(self, amount_to_convert: float, to_currency: str) -> bool:
        if to_currency == "usd":
            from_currency = "nis"
            if self.__allowed_usd:
                if self.withdraw(amount_to_convert, "nis"):
                    usd_amount = amount_to_convert / self.rate
                    self.deposit(usd_amount, "usd")
                else:
                    return False
            else:
                return False
        else:
            from_currency = "usd"
            if self.withdraw(amount_to_convert, "usd"):
                nis_amount = amount_to_convert * self.rate
                self.deposit(nis_amount, "nis")
            else:
                return False
        self._add_transaction(self._create_tx_log("convert", from_currency, amount_to_convert))
        return True

    def get_current_balance(self, currency: str) -> float | bool:
        if currency == "usd":
            if self.__allowed_usd:
                return self.__usd_balance
            return False
        return self.__shekel_balance

    def get_transactions_per_date(self, tx_date: str) -> list[dict] | bool:
        if self.__transaction_data.get(tx_date):
            return self.__transaction_data[tx_date]
        return False

    def get_monthly_cash_flow(self, month_to_flow: str, year_to_flow: str):
        to_account = 0
        from_account = 0
        for k, v in self.__transaction_data.items():
            year, month, _ = k.split("-")
            if month_to_flow == month and year_to_flow == year:
                for tx in v:
                    if tx["type"] == "deposit":
                        to_account += tx["amount"]
                    elif tx["type"] == "withdraw":
                        from_account += tx["amount"]
        return to_account, from_account

    def get_annual_cash_flow(self, year_to_flow: str):
        to_account = 0,
        from_account = 0
        for k, v in self.__transaction_data.items():
            year, _, _ = k.split("-")
            if year_to_flow == year:
                for tx in v:
                    if tx["type"] == "deposit":
                        to_account += tx["amount"]
                    elif tx["type"] == "withdraw":
                        from_account += tx["amount"]
        return to_account, from_account


