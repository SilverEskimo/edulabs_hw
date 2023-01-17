from example.BankAccount import *

if __name__ == '__main__':
    acc_holder = {
            "passport_num": 123123,
            "name": "Daniel",
            "address": "Rishon",
            "phone": 1023123
    }
    daniel_ba = BankAccount(321321, acc_holder, 0, 0, 100, True)

    if daniel_ba.deposit(200, "nis"):
        print("Success deposit")
    else:
        print("Failed Deposit")

    # if daniel_ba.withdraw(500, "nis"):
    #     print("Success withdraw")
    # else:
    #     print("Failed withdraw")

    if daniel_ba.convert(100, "nis"):
        print("Convert done")
    else:
        print("Convert failed")

    print(daniel_ba.get_current_balance("nis"))
    print(daniel_ba.get_current_balance("usd"))
    print(daniel_ba.get_transactions_per_date("2023-01-17"))

