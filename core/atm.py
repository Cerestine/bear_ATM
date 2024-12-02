from core.bank import bankApi

def atm_card_reader_handler():
    # function to call card reader HW and return card data(PIN)
    card_data = 11223344
    return card_data


class simpleAtm:
    def __init__(self):
        self.bank = bankApi()
        self.card_reader_handler = atm_card_reader_handler()
        self.valid = False

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
        pass

    def _close_cash(self):
        pass

    def _count_cash(self):
        pass

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
        
    def bank_transaction(self, selection, data=None):
        if selection == 1:
            action = "balance"
        elif selection == 2:
            action = "deposit"
        elif selection == 3:
            action = "withdraw"
        result, result_data = self.bank.bank_request(action, data)
    
    def cash(self):
        self._open_cash()
        self._count_cash()
        self._close_cash()
        pass
