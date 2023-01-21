from lesson10.c3_bank_account_new.BankAccount import *


if __name__ == '__main__':
    bank_account = BankAccount(
        1234567,
        {
            "name": "Slava",
            "passport_num": 87654321,
            "address": "Rehovot",
            "phone": "0528381023"
        },
        200,
    )

    bank_account1 = BankAccount(
        1234567,
        {
            "name": "Slava",
            "passport_num": 87654321,
            "address": "Rehovot",
            "phone": "0528381023"
        },
        200,
    )
    print(bank_account.get_current_balance("nis"))
    bank_account += 100
    print(bank_account.get_current_balance("nis"))

