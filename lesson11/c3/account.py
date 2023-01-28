class Account:
    def __init__(self, account_id: int, branch_id: int, owners: list[int]):
        self._account_id = account_id
        self._branch_id = branch_id
        self._owners_ids = owners
        self._balance = 0

    def deposit(self, amount: float):
        if amount <= 0:
            return False
        self._balance += amount
        return True

    def withdraw(self, amount: float):
        if amount <= 0 or self._balance - amount < 0:
            return False
        self._balance -= amount
        return True

    def get_branch(self):
        return self._branch_id

    def get_owners_ids(self):
        return self._owners_ids

    def __str__(self):
        return f"Account ID:{self._account_id}\nBranch ID: {self._branch_id}"

