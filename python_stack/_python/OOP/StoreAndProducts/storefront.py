import store
import product

mikesGoods = store.Store("Mike's Goods")
mikesGoods.add_product(product.Product("Iron Sword", 10, "Swords")).add_product(product.Product("Steel Sword", 15, "Swords")).add_product(product.Product("Health Potion", 25, "Potions")).add_product(product.Product("Strength Potion", 30, "Potions")).add_product(product.Product("Wish Potion", 1000000, "Potions"))

mikesGoods.show_inventory()

mikesGoods.sell_product(mikesGoods.products[3].id)
print("\n")
mikesGoods.show_inventory()
mikesGoods.inflation(0.005).show_inventory()
mikesGoods.set_clearance("Swords",0.5).show_inventory()
