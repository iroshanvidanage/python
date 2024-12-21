class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        # Implement the logic to add an item to the order

    def get_total(self):
        # Implement the logic to calculate the total cost of the order

# Example Usage
customer = Customer("John Doe", "john@example.com")
order = Order(customer)

product1 = Product("Laptop", 999.99)
product2 = Product("Mouse", 49.99)

order.add_item(product1, 1)
order.add_item(product2, 2)

total = order.get_total()
