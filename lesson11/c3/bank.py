import datetime

from branch import Branch
from account import Account
from customer import Customer


class Bank:
    def __init__(self, bank_name: str, hq_address: str):
        self._bank_name = bank_name
        self._hq_address = hq_address
        self._branches_by_id: dict[int, Branch] = {}
        self._accounts_by_id: dict[int, Account] = {}
        self._customers_by_id: dict[int, Customer] = {}
        self._accounts_with_owners: dict[int, [Customer]]

    def update_branch_address(self, branch_id: int, new_address: str) -> bool:
        branch = self._branches_by_id.get(branch_id)
        if not branch:
            return False
        branch.set_address(new_address)
        return True

    def add_branch(self, branch_id: int, branch_name: str, branch_address: str, branch_city: str) -> Branch | bool:
        if self._branches_by_id.get(branch_id):
            return False
        new_branch = Branch(branch_id, branch_name, branch_address, branch_city)
        self._branches_by_id[ branch_id ] = new_branch
        return new_branch

    def get_branch_by_id(self, branch_id) -> Branch | bool:
        if not self._branches_by_id.get(branch_id):
            return False
        return self._branches_by_id[branch_id]

    def get_branches_by_city(self, branch_city: str) -> list[Branch] | bool:
        branches_list = []
        for branch_id, branch in self._branches_by_id.items():
            if branch.get_branch_city() == branch_city.lower():
                branches_list.append(branch)
        return branches_list

    def delete_branch(self, branch_id: int) -> bool:
        if not self._branches_by_id.get(branch_id):
            return False
        for account_id, account in self._accounts_by_id.items():
            if account.get_branch() == branch_id:
                print("Cannot remove a branch with at least one active account")
                return False
        self._branches_by_id.pop(branch_id)
        return True

    def add_account(self, account_id: int, branch_id: int, owner_ids: list[int]) -> Account | bool:
        if self._accounts_by_id.get(account_id):
            return False
        account = Account(account_id, branch_id, owner_ids)
        self._accounts_by_id[account_id] = account
        return account

    def get_account_by_id(self, account_id) -> Account | bool:
        if not self._accounts_by_id.get(account_id):
            return False
        return self._accounts_by_id[account_id]

    def add_customer(self,
                     customer_id: int,
                     first_name: str,
                     last_name,
                     address: str,
                     credit_score: int,
                     bdate: datetime.date,
                     account: Account) -> Customer | bool:
        if self._customers_by_id.get(customer_id):
            return False
        customer = Customer(customer_id, first_name.lower(), last_name.lower(),
                            address.lower(), credit_score, bdate, account)
        self._customers_by_id[customer_id] = customer
        return customer

    def get_customer_by_id(self, customer_id: int):
        if not self._customers_by_id.get(customer_id):
            return False
        return self._customers_by_id[customer_id]

    def get_customer_by_name(self, customer_full_name: str) -> Customer | bool:
        for customer_id, customer in self._customers_by_id.items():
            if customer.get_customer_full_name() == customer_full_name.lower():
                return customer
        return False

    def update_customer_details(self, customer_name=False, address=False, add_branch=False):
        pass

    def delete_customer(self, customer_id: int) -> bool:
        if not self.get_customer_by_id(customer_id):
            return False
        for account_id, account in self._accounts_by_id:
            owners = account.get_owners_ids()
            for owner in owners:
                if owner == self._customers_by_id[customer_id].get_customer_id() and len(owners) == 1:
                    print("Cannot delete a customer with an active account")
                    return False
        self._customers_by_id.pop(customer_id)
        return True

    def transfer(self, from_account_id: int, to_account_id: int, amount: float) -> bool:
        if not (self.get_account_by_id(from_account_id) or self.get_account_by_id(to_account_id)):
            return False
        from_account = self.get_account_by_id(from_account_id)
        to_account = self.get_account_by_id(to_account_id)
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

    def get_accounts_by_holder_id(self, customer_id) -> list[Account] | bool:
        if not self.get_customer_by_id(customer_id):
            return False
        return self.get_customer_by_id(customer_id).get_customer_accounts()








