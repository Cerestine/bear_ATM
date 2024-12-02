import bankRESTApi

class bankApi:
    def __init__(self):
        self.bank_REST_API_Handle = bankRESTApi()
        self.validation = False

    def _callback(self, result):
        callback_result = False
        if result == "200":
            callback_result  = True
            callback_text = None
        elif result == "300":
            callback_text = "Bank transaction failed"
        elif result == "400":
            callback_text = "Bank connnection failed"
        elif result == "401":
            callback_text = "Bank disconnnection failed"
        return callback_result, callback_text

    def _connect(self):
        # connnects to bank sever
        return self.bank_REST_API_Handle.connect()

    def _disconnect(self):
        # disconnnects to bank sever
        return self.bank_REST_API_Handle.disconnect()

    def _reqest(self, action, data):
        result_data = None
        # connnects to bank sever
        if self._connect():
            # the bank API need 2 inputs.
            # action -> validation, balance, deposit, withdraw, account
            # data -> data corresponding with above action. [Account number, cash]
            # result_data -> Final balance of account after transaction. None for validation
            # bank API must return if request is succesfull or not as boolean
            result, result_data = self.bank_REST_API_Handle.request(action, data)
            if result:
                result = "200"
            else:
                result = "300"
            if not self._disconnect():
                result = "401" 
        else:
            result = "400"
        return result, result_data

    def bank_request(self, action, data=None):
        """
            args:
                action(str): validation, balance, deposit, withdraw, account
            returns:
                callback_result(bool): True if requset is successful, False if there is any error
                result_data(object): requested data object else None
        """
        try:
            result, result_data = self._reqest(action, data)
            callback_result, callback_text = self._callback(result)
        except Exception as callback_text:
                print(callback_text)
        finally:
            self.validation = callback_result
            return callback_result, result_data
