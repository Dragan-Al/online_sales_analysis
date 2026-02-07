class Cart:
    def __init__(self):
        self.cart_items = []

    def add_cart(self, product):
        self.cart_items.append(product)
        print(f"Added {product.name} to the cart.")

    def total_amount(self):
        return sum(product.price * product.quantity for product in self.cart_items)
    
    def show_cart(self):
        for product in self.cart_items:
            print(f"- {product.show_product()}")
