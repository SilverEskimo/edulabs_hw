import datetime
from account import Account


class Customer:
    def __init__(self,
                 customer_id: int,
                 customer_fist_name: str,
                 customer_last_name: str,
                 customer_address: str,
                 customer_credit_score: float,
                 customer_bdate: datetime.date,
                 customer_account: Account):
        self._id = customer_id
        self._fist_name = customer_fist_name
        self._last_name = customer_last_name
        self._credit_score = customer_credit_score
        self._address = customer_address
        self._bdate = customer_bdate
        self._accounts = [customer_account]

    def get_customer_accounts(self):
        return self._accounts

    def get_customer_id(self):
        return self._id

    def get_customer_full_name(self):
        return self._fist_name + " " + self._last_name

    def __str__(self):
        return f"{self._id},{self._fist_name},{self._last_name}"


