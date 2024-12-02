from time import sleep
from core.bank import bankApi

def atm_card_reader_handler():
    # function to call card reader HW and return card data(PIN)
    card_data = 11223344
    return card_data


class simpleAtm:
    def __init__(self):
        self.bank = bankApi()
        self.card_reader_handler = atm_card_reader_handler()
        self.cash_open_time = 5
        self.valid = False
        self.account = 0

    def _callback(self, data):
        # TODO: implement callback for errors
        if data:
            pass
        else:
            self.valid = data
            print("Invalid Card. Please insert correct card")


    def _validate_PIN(self, card_data) -> bool:
        result, _ = self.bank.bank_request("validation", card_data)
        self._callback(result)
        return result

    def _get_accounts(self) -> list:
        result, result_data = self.bank.bank_request("account")
        self._callback(result_data)
        return 

    def _open_cash(self):
        # Open cash depensor
        self.card_reader_handler.open_cash()

    def _close_cash(self):
        # close cash depensor
        self.card_reader_handler.close_cash()

    def _out_cash(self, cash_num):
        # Transfer cash from holdings in ATM to depensor
        self.card_reader_handler.out_count_cash(cash_num)

    def _store_cash(self):
        # store cash in cash depensor
        self.card_reader_handler.store_cash()

    def _count_cash(self):
        # Count cash in depensor
        # returns counted cash
        return self.card_reader_handler.count_cash()

    def _deposit(self):
        cash_check = "n"
        self._open_cash()
        sleep(self.cash_open_time)
        self._close_cash()
        cash = self._count_cash()
        while cash_check.lower() == "n":
            cash_check = input(f"Deposit amount: {cash} correct? (Y/N)")
            self._open_cash()
            sleep(self.cash_open_time)
            self._close_cash()
            cash = self._count_cash()
        self._store_cash()
        return cash

    def _withdraw(self, cash_num):
        self._out_cash(cash_num)
        cash = self._count_cash()
        while cash_num != cash:
            self._out_cash(abs(cash_num-cash))
        self._open_cash()
        sleep(self.cash_open_time)
        self._close_cash()
        cash = self._count_cash()
        while cash != 0:
            print("Please check ATM")
            self._open_cash()
            sleep(self.cash_open_time)
            self._close_cash()
            cash = self._count_cash()
        return cash

    def card_reader(self):
        """
            Reads card data from card reader HW

            returns -> valid_card(Bool): True if PIN number is valid, False is not 
        """
        # read card data from card reader and return PIN data
        self.valid = False
        card_data = self.card_reader_handler()
        valid_card = self._validate_PIN(card_data)
    
        return valid_card

    def get_bank_account(self):
        result = ["Cancel"]
        bank_account = self._get_accounts()
        for account in bank_account:
            result.append(account)
        return result

    def bank_transaction(self, selection, account_num=None, cash=None):
        if selection == 1:
            action = "balance"
        elif selection == 2:
            action = "deposit"
        elif selection == 3:
            action = "withdraw"
        result, result_data = self.bank.bank_request(action, data=[account_num, cash])
        return result, result_data
    
    def cash(self, cash_num=None):
        if cash_num is None:
            cash = self._deposit()
        else:
            cash = self._withdraw(cash_num)
            while cash != 0:
                print("Please check ATM")
                self._open_cash()
                sleep(5)
                self._close_cash()
                cash = self._count_cash()
        return cash

    def reset(self):
        self.bank.validation = False
        self.valid = False
