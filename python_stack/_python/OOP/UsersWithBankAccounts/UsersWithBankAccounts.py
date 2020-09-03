
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

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    def open_an_account(self, account):
        self.accounts[account.name] = account
        return self
    def make_deposit(self,account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self
    def make_withdrawl(self,account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self
    def display_user_balance(self):
        print("\n",self.name,"Accounts:")
        for k in self.accounts:
            print("\n")
            self.accounts[k].display_account_info()
        return self
    def transfer_money(self, other_user, amount, account_name, other_user_account_name):
        print("Transferring:", amount, "from", account_name, "to", other_user_account_name)
        self.accounts[account_name].withdraw(amount)
        other_user.accounts[other_user_account_name].deposit(amount)
        return self

pen = User("Pen")
pen.open_an_account(BankAccount(0.25, 100, "Niran Mercenaries Official Account")).make_deposit("Niran Mercenaries Official Account", 700).make_deposit("Niran Mercenaries Official Account",1000).display_user_balance().make_withdrawl("Niran Mercenaries Official Account", 350).display_user_balance().open_an_account(BankAccount(0.15,100,"Pen's Personal Account")).transfer_money(pen, 50,"Niran Mercenaries Official Account","Pen's Personal Account").display_user_balance()