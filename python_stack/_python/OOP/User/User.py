
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdrawl(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(self.name, "Current Balance:", self.balance)
    def transfer_money(self, other_user, amount):
        print("Transferring:", amount, "from", self.name, "to", other_user.name)
        self.balance -= amount
        other_user.balance+=amount

berg = User("Berg")
draught = User("Draught")
pen = User("Pen")

berg.make_deposit(200)
berg.make_deposit(200)
berg.make_deposit(50)
berg.make_withdrawl(300)
berg.display_user_balance()

draught.make_deposit(400)
draught.make_deposit(400)
draught.make_withdrawl(200)
draught.make_withdrawl(100)
draught.display_user_balance()

pen.make_deposit(2000)
pen.make_withdrawl(100)
pen.make_withdrawl(100)
pen.make_withdrawl(100)
pen.display_user_balance()

berg.transfer_money(pen, 50)
berg.display_user_balance()
pen.display_user_balance()


