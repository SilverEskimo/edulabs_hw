from lesson9.c3_bank_account.BankAccount import *


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
        allowed_usd=True
    )
    bank_account.deposit(150, "nis")
    if bank_account.deposit(200, "usd"):
        print("Done deposit 200 usd")
    else:
        print("Something went wrong")
    if bank_account.withdraw(100, "nis"):
        print("Done withdraw 100 NIS")
    else:
        print("Something went wrong")
    if bank_account.convert(50, "usd"):
        print("Converted 50 nis")
    else:
        print("Something went wrong with convert")
    print("Nis balance:", bank_account.get_current_balance("nis"))
    print("USD balance:", bank_account.get_current_balance("usd"))
    print(bank_account.get_transactions_per_date("2023-01-15"))
    inflow, outflow = bank_account.get_monthly_cash_flow("01", "2023")
    print(f"In month 01, year 2023 the cash flow is:\nInflow: {inflow}\nOutflow: {outflow}")