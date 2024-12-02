from time import sleep
from core.atm import simpleAtm

if __name__ == "__main__":
    atm = simpleAtm()
    print("Insert Card to see Balance/Deposit/Withdraw")
    while True:
        if atm.card_reader():
            account_num = input("Select bank account: (Press 0 to cancel transaction)")
            if account_num != 0:
                bank_accounts = atm.bank_account()
                # TODO: print bank accounts
                for key, value in bank_accounts.items():
                    print()
                # TODO: get account selection
                # TODO: get transaction
                # TODO: print transaction result
        sleep(1)
