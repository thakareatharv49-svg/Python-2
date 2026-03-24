class bank_account:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited {amount}.New balance:{self.balance}")
        else:
            print("deposited amount cannot be negative") 
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"withdrawn {amount}.New balance:{self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("withdrawn amount cannot be negative")    
    def check_balance(self):
        print(f"current balance:{self.balance}")
account=bank_account("11234456",1000)
account.deposit(200)
account.withdraw(100)
account.check_balance()
