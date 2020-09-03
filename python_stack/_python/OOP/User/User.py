
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(self.name, "Current Balance:", self.balance)
        return self
    def transfer_money(self, other_user, amount):
        print("Transferring:", amount, "from", self.name, "to", other_user.name)
        self.balance -= amount
        other_user.balance+=amount
        return self

berg = User("Berg")
draught = User("Draught")
pen = User("Pen")

berg.make_deposit(200).make_deposit(200).make_deposit(50).make_withdrawl(300).display_user_balance()

draught.make_deposit(400).make_deposit(400).make_withdrawl(200).make_withdrawl(100).display_user_balance()

pen.make_deposit(2000).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100).display_user_balance()

berg.transfer_money(pen, 50).display_user_balance()
pen.display_user_balance()


