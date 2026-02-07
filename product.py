class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product(self):
        return f"Product: {self.name}, Price {self.price} euros, Quantity: {self.quantity}"
    
    def update_product(self, new_quantity):
        self.quantity = new_quantity
        print(f"Quantity of {self.name} has been updatet to {self.quantity}")
