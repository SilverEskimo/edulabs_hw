import datetime
from threading import Lock


class BankAccount:
    def __init__(self, owner_id: int, full_name: str):
        self._owner_id = owner_id
        self._full_name = full_name
        self._balance = 0
        self._transactions_list = []
        self._balance_lock = Lock()
        self._general_lock = Lock()

    @staticmethod
    def lock(function: callable):
        if function.__name__ in ("balance", "deposit", "withdraw"):
            def wrapping_function(*args, **kwargs):
                with args[0].get_balance_lock():
                    return function(*args, **kwargs)
        else:
            def wrapping_function(*args, **kwargs):
                with args[0].get_general_lock():
                    return function(*args, **kwargs)
        return wrapping_function

    @property
    @lock
    def balance(self):
        return self._balance

    @balance.setter
    @lock
    def balance(self, amount: float):
        self._balance += amount

    @lock
    def deposit(self, amount_to_deposit):
        self._balance += amount_to_deposit
        self.tx_history = amount_to_deposit

    @lock
    def withdraw(self, amount_to_withdraw: float):
        self._balance -= amount_to_withdraw
        self.tx_history = amount_to_withdraw

    @property
    def tx_history(self):
        return self._transactions_list

    @tx_history.setter
    @lock
    def tx_history(self, amount: float):
        self._transactions_list.append(amount)

    def get_balance_lock(self):
        return self._balance_lock

    def get_general_lock(self):
        return self._general_lock
