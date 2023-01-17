# deposit() - add cash to account
# withdraw() - withdraw cash from account. Think about state consistency!
# convert() - convert specified amount from shekels to usd or vise versa inside the account if applicable.
# Think about edge cases!
from datetime import date
class BankAccount:
    def __init__(
            self,
            account_number: int,
            acc_holder: dict,
            nis_balance: float,
            usd_balance: float,
            credit_limit: float
    ):
        self.account_number = account_number
        self.account_holder = {
            "passport_num": acc_holder["passport_num"],
            "name": acc_holder["name"],
            "address": acc_holder["address"],
            "phone": acc_holder["phone"]
        }
        self.nis_balance = nis_balance
        self.usd_balance = usd_balance
        self.credit_limit = credit_limit
        self.transactions_data = {}

    #    "17-01-2023": [
    #                 {
    #                     "type": "deposit",
    #                     "amount": 100
    #                 },
    #                 {
    #                     "type": "withdraw",
    #                     "amount": 50
    #                 }
    #             ]

    def deposit(self, deposit_amount: float, currency: str) -> bool:
        action_date = str(date.today())
        if currency == "usd":
            self.usd_balance += deposit_amount
            self.update_transaction_data(action_date, "deposit", deposit_amount, "usd")
            return True
        self.nis_balance += deposit_amount
        self.update_transaction_data(action_date, "deposit", deposit_amount, "nis")
        return True

    def withdraw(self, withdraw_amount: float, currency: str) -> bool:
        action_date = str(date.today())
        if currency == "usd" and self.usd_balance - withdraw_amount >= 0:
            self.usd_balance -= withdraw_amount
            self.update_transaction_data(action_date, "withdraw", withdraw_amount, "usd")
            return True
        elif currency == "nis" and self.nis_balance - withdraw_amount >= -self.credit_limit:
            self.nis_balance -= withdraw_amount
            self.update_transaction_data(action_date, "withdraw", withdraw_amount, "nis")
            return True
        return False

    def convert(self, convert_amount: float, from_currency: str) -> bool:
        action_date = str(date.today())
        if from_currency == "usd" and self.withdraw(convert_amount, "usd"):
            nis_amount = convert_amount * 3.5
            self.deposit(nis_amount, "nis")
            self.update_transaction_data(action_date, "convert", convert_amount, "usd")
            return True
        elif from_currency == "nis" and self.withdraw(convert_amount, "nis"):
            usd_amount = convert_amount / 3.5
            self.deposit(usd_amount, "usd")
            self.update_transaction_data(action_date, "convert", convert_amount, "nis")
            return True
        return False

    def get_current_balance(self, currency: str):
        if currency == "usd":
            return self.usd_balance
        return self.nis_balance

    def get_transactions_per_date(self, some_date: str) -> list[dict]:
        return self.transactions_data[some_date]

    def update_transaction_data(self, some_date: str, action: str, amount: float, currency: str):
        res = {
            "action": action,
            "amount": amount,
            "currency": currency
        }
        if self.transactions_data.get(some_date):
            self.transactions_data[some_date].append(res)
        else:
            self.transactions_data[some_date] = [res]

