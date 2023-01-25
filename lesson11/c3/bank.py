from branch import Branch
from account import Account


class Bank:
    def __init__(self, bank_name: str, hq_address: str):
        self._bank_name = bank_name
        self._hq_address = hq_address

        self._branches_by_id: dict[int, Branch] = {}
        self._accounts_by_id: dict[int, Account] = {}

    def update_branch_address(self, branch_id: int, new_address: str) -> bool:
        branch = self._branches_by_id.get(branch_id)
        if not branch:
            return False
        branch.set_address(new_address)
        return True

    def add_account(self, account_id: int, branch_id: int):
        account = Account(account_id, branch_id)
        self._accounts_by_id[account_id] = account



