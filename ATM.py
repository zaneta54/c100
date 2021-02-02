 class atm :
    def __init__(self,cashWithdrawal,bankEnquiry):
        self.b = bankEnquiry
        self.c=cashWithdrawal
    def start (self):
        print ('start')

bank = atm("$100","call bank") 
print(bank.c)