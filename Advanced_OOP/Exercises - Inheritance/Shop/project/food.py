from project import Product

class Food(Product):
    def __init__(self, name: str, quantity: int = 15):
        super().__init__(name, quantity)
