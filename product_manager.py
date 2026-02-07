class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product.show_product())

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product {name} hes been removed.")
        print(f"No product found with name {name}.")
