from concurrent.futures import ThreadPoolExecutor
from lesson18.E8.bank_account import BankAccount

if __name__ == '__main__':
    account = BankAccount(123456, "Israel Israeli")

    def multiple_transactions_deposit(account):
        for i in range(100, 2000000, 10):
            account.deposit(i)

    def multiple_transactions_withdraw(account):
        for i in range(100, 2000000, 10):
            account.withdraw(i)


    with ThreadPoolExecutor(4) as executor:
        executor.submit(multiple_transactions_deposit, account)
        executor.submit(multiple_transactions_withdraw, account)

    assert account.balance == 0, \
        f"Expected balance: 0, received: {account.balance}"

    assert len(account.tx_history) == 399980, \
        f"Expected transactions: 399980, received: {len(account.tx_history)}"
