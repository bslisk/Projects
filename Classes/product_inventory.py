# Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand.
# Then create an *inventory* class which keeps track of various products and can sum up the inventory value.
from random import random, randint


class Product():
    def __init__(self, price: float, id: int, quantity: int) -> None:
        self.price = price
        self.id = id
        self.quantity = quantity


class Inventory():
    def __init__(self) -> None:
        self.products = []

    def calculate_value(self) -> float:
        total_value = 0
        for product in self.products:
            total_value += (product.price * product.quantity)
        return total_value

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, id: int) -> bool:
        for i in range(len(self.products)):
            if self.products[i].id == id:
                self.products.pop(i)
                return True
        return False

    def get_product(self, id: int) -> Product:
        for i in range(len(self.products)):
            if self.products[i].id == id:
                return self.products[i]
        return None


def main():
    inventory = Inventory()

    print('Adding products...\n')
    for i in range(1, 11):
        price = round(random() * 100, 2)
        quantity = randint(1, 200)
        product = Product(price, i, quantity)
        inventory.add_product(product)
        print(f'Product {i}. Price: {price}, id: {i}, quantity: {quantity}.')

    print('\n')
    print(f'Inventory value: {inventory.calculate_value()}')


if __name__ == '__main__':
    main()
