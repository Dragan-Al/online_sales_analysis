class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(f"Product {product['name']}, \nCena: {product['price']}, \nQuantity: {product['quantity']}")

    def total_value(self):
        total = 0
        for product in self.products:
            total += product["price"] * product["quantity"]
        return total