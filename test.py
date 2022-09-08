class Account(object):
    lastaccno = 0 #Class variable - keeps track of the last account number
    def __init__(self, initialdeposit):
        Account.lastaccno += 1
        self.acctno = str(Account.lastaccno).zfill(10)
        self.balance = initialdeposit
        
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        
    
    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            return "Withdrawal successful"
        else:
            return "Insufficient amount"
    
    def __str__(self):
        return (f"Account {self.acctno} has a balance of ${self.balance:.2f}.")


class Savings (Account):
    def __init__(self, initialdeposit):
        super().__init__(initialdeposit)
        self.interest = 0.5
        
    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self, amount):
        return super().withdraw(amount)
            
    def __str__(self):
        return (f"Savings Account {self.acctno} has a balance of ${self.balance:.2f}.")
        

class Checking (Account):
    def __init__(self, initialdeposit):
        super().__init__(initialdeposit)
    
    def deposit(self, amount):
        return super().deposit(amount)
    
    def withdraw(self, amount):
        return super().withdraw(amount)
        
    def __str__(self):
        return (f"Checking Account {self.acctno} has a balance of ${self.balance:.2f}.")

firstacc = Account(1000)
secondacc = Account(2000.67)
savings = Savings(1000)
checking = Checking(1000)

