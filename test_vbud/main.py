class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}, {self.price}'


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        return product

    def total_price(self):
        return sum(item.price for item in self.items)

    def most_expensive(self):
        return max(self.items, key=lambda item: item.price)

    def apply_discount(self, discount_percentage):
        total = self.total_price()
        discounted_price = total * (1 - discount_percentage/100)
        return f"Total price after {discount_percentage}% discount: {discounted_price:.2f}"

    def clear_cart(self):
        self.items = []
        return "Cart is now empty."


product1 = Product("Laptop", 1000)
product2 = Product("Phone", 500)
product3 = Product("Tablet", 300)


cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print("cart:", cart.items)
print("total:", cart.total_price())
print(cart.most_expensive())
print(cart.apply_discount(40))

print(cart.clear_cart())
print("cart:", cart.items)



