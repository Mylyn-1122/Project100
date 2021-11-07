#atm.py

class Atm(object):
    def __init__(self, cardNumber, pinNumber, balanceAmount):
        self.cardnumber = cardNumber
        self.pin = pinNumber
        self.amount = balanceAmount

    def CashWithdrawl(self):
        print("You Have withdrawn cash")
    
    
    def Deposit(self):
        print("you have deposited cash")

Card = Atm(111, 111, 120)
print(Card.Deposit())
