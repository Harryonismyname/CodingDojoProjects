class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, id):
        if isinstance(id, str):
            for p in range(len(self.products)-1):
                if self.products[p].id == id:
                    print("Selling:")
                    self.products[p].print_info()
                    self.products.pop(p)
        else:
            self.products[id].print_info()
            self.products.pop(id)
        return self
    def show_inventory(self):
        for i in self.products:
            i.print_info()
        print("\n")

    def inflation(self, percent_increase):
        print("Inflation!\nPrices are rising!")
        for i in self.products:
            i.update_price(percent_change=percent_increase, is_increased=True)
        return self
    def set_clearance(self, category, percent_discount):
        print("Selling:", category, percent_discount,"Off!")
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_change=percent_discount, is_increased=False)
        return self
