class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount):
        super().__init__(name, price, quantity)
        self.discount = discount

    def discounted_price(self):
        return self.price * (1 - self.discount)

object1 = Product("Laptop", 1000, 5)
object2 = DiscountedProduct("Smartphone", 500, 10, 0.2)
object3 = DiscountedProduct("Headphones", 100, 15, 0.1)

print(f"Product: {object1.name}, Price: {object1.price}, Quantity: {object1.quantity}, Discounted Price: N/A")
print(f"Product: {object2.name}, Price: {object2.price}, Quantity: {object2.quantity}, Discounted Price: {object2.discounted_price()}")
print(f"Product: {object3.name}, Price: {object3.price}, Quantity: {object3.quantity}, Discounted Price: {object3.discounted_price()}")