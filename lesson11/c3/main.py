import datetime

from lesson11.c3.account import Account
from lesson11.c3.bank import Bank
from lesson11.c3.branch import Branch
from lesson11.c3.customer import Customer

if __name__ == '__main__':

    bank = Bank(
        "Slava",
        "Haruv 8, Ekron"
    )

    branch = bank.add_branch(1, "Dada", "8st west", "Tel Aviv")
    account = bank.add_account(98765, 1, [123])
    customer = bank.add_customer(
        123,
        "slava",
        "sereb",
        "Migdal HaLevanon 38, Modiin",
        90,
        datetime.date(year=1990, month=10, day=2),
        account
    )
    bank.add_branch(2, "Dudu", "7th east", "NY")

    print(bank.get_customer_by_id(123))
    print(bank.get_customer_by_name("Slava Sereb"))


