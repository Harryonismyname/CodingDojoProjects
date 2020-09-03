from random import randint
class Product:
    def __init__(self, name, price, category):
        self.name= name
        self.price = price
        self.category = category
        self.id = self.set_id()
    def set_id(self):
        id = ""
        for x in range(4):
            id+=str(randint(0,9))
        return id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price*percent_change
        else:
            self.price-= self.price*percent_change
        return self
    def print_info(self):
        print(self.name, self.category, self.price, self.id)
        return self
