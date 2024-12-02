from time import sleep
from core.atm import simpleAtm

if __name__ == "__main__":
    atm = simpleAtm()
    print("Insert Card to see Balance/Deposit/Withdraw")
    while True:
        if atm.card_reader():
            bank_accounts = atm.get_bank_account()
            if len(bank_accounts) > 1:
                for i, accounts in enumerate(bank_accounts):
                    print(f"{i}: {accounts}")
                account_num = input("Select bank account: (Press 0 to cancel transaction)")
                if account_num == 0:
                    atm.reset()
                    print("Canceling transactions")
                else:
                    while True:
                        print("1: See balance")
                        print("2: Deposit")
                        print("3: Withdraw")
                        transaction_num = input("Select transaction: (Press 0 to cancel transaction)")
                        if transaction_num < 4:
                            if transaction_num == 0:
                                atm.reset()
                                print("Canceling transactions")
                            elif transaction_num == 1:
                                result, balance = atm.bank_transaction(transaction_num, bank_accounts[account_num])
                            elif transaction_num == 2:
                                cash = atm.cash()
                                result, balance = atm.bank_transaction(transaction_num, bank_accounts[account_num])
                            elif transaction_num == 3:
                                cash_num = input("Input amount")
                                chash = atm.cash(cash_num)
                                result, balance = atm.bank_transaction(transaction_num, bank_accounts[account_num], cash_num)
                            print(f"Current balance of account: {bank_accounts[account_num]} is ${balance}")
                            break
                        else:
                            print("Wrong input please try again")
            else:
                print("No account present. Please try again")
        sleep(1)
