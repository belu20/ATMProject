from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance=10000) :
        self.id = id
        self.Pin = custPin
        self.Balance = custBalance
    
    def checkid(self):
        return self.id
    def checkPin(self):
        return self.Pin
    def checkBalance(self):
        return self.Balance

    def withdrawBalance(self, nominal):
        self.Balance -= nominal
    def depositBalance(self, nominal):
        self.Balance += nominal

        