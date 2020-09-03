class BankAccount:
    def __init__(self, int_rate=0.01, balance=0, name=""):
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("{}\nBalance: ${}\nIntrest Rate: {}".format(self.name,self.balance, self.int_rate))
        return self
    def yield_intrest(self):
        if self.balance > 0:
            self.balance+=self.int_rate*self.balance
        return self

niranBankAndTrust= BankAccount(0.15, 2000,"Niran Bank and Trust Account")
firstEmpireCreditUnion= BankAccount(0.25,100, "First Empire Credit Union Account")

niranBankAndTrust.deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_intrest().display_account_info()

firstEmpireCreditUnion.deposit(9000).deposit(900).withdraw(100).withdraw(100).withdraw(100).withdraw(600).yield_intrest().display_account_info()