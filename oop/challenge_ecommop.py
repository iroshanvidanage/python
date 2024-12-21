class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def __str__(self) -> str: return f'Product(name={self.name}, price={self.price})'

class Customer:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
    
    def __str__(self) -> str: return f'Customer(name={self.name}, email={self.email})'

class Order:
    def __init__(self, customer) -> None:
        self.customer = customer
        self.items = {}

    def add_item(self, product: Product, quantity: float) -> None:
        # Implement the logic to add an item to the order
        if quantity <= 0: # edge case handling
            print(f"Cannot add {quantity} of {product.name}. Quantity should be positive.")
            return
        if product in self.items: # same item if multiple times added
            self.items[product] += quantity
        else: # new item
            self.items[product] = quantity

    def get_total(self) -> float:
        # Implement the logic to calculate the total cost of the order
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total
    
    @property 
    def total(self) -> float: return sum(product.price * quantity for product, quantity in self.items.items())
    
    def __str__(self) -> str: return f'Order(customer={self.customer}, items={self.items})'

# Example Usage
def test_example() -> None:
    customer = Customer("John Doe", "john@example.com")
    order = Order(customer)

    product1 = Product("Laptop", 999.99)
    product2 = Product("Mouse", 49.99)

    order.add_item(product1, 1)
    order.add_item(product2, 2)
    order.add_item(product2, 0) # Test adding zero quantity

    total = order.get_total()
    print(f"Total Order Cost: ${total:.2f}")

    print(f"Total Order Cost using @property: ${order.total:.2f}")


if __name__ == '__main__':
    test_example()