class ATM():
    def __init__(self,CardNumber,PinNumber):
        self.CardNumber = CardNumber
        self.PinNumber = PinNumber
        
    def withdrawl(self):
        print("withdrawl")
        
    def balanceInquiry(self):
        print("balanceInquiry")
    
card = ATM("536r", "3464")
card.withdrawl()
card.balanceInquiry()
    
