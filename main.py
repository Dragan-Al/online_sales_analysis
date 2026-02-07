from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Laptop", 1200, 2))
manager.add_product(Product("Mouse", 25, 5))
manager.add_product(Product("Keyboard", 75, 3))
manager.add_product(Product("Monitor", 300, 1))

print("Products: ")
manager.display_products()

print(f"Total value: {manager.total_value()} euros")

manager.remove_product("Mouse")
print("\n Products after removal: ")
manager.display_products()
print(f"Total inventory value: {manager.total_value()} euros")
manager.add_product(Product("Laptop", 1350, 2))
manager.add_product(Product("Mouse", 20, 5))
manager.add_product(Product("Keyboard", 85, 3))
manager.add_product(Product("Monitor", 500, 1))

print("Products: ")
manager.display_products()

print(f"Total value: {manager.total_value()} euros")

manager.remove_product("Mouse")
print("\n Products after removal: ")
manager.display_products()
print(f"Total inventory value: {manager.total_value()} euros")

cart = Cart()

print("\n----------------\n")

cart.add_cart(manager.products[0])  
cart.add_cart(manager.products[1])  
cart.add_cart(manager.products[2]) 

print("\nCart: ")
cart.show_cart()

print(f"\n Total amount to pay: {cart.total_amount()} euros")