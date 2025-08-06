from abc import ABC, abstractmethod
from products.base_product import BaseProduct


class BaseStore(ABC):
    PROFIT_FACTOR = 0.1

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value.strip()) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        profit = sum(p.price for p in self.products) * self.PROFIT_FACTOR
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    @abstractmethod
    def store_type(self) -> list[str]:
        """List of allowed product sub_types."""
        pass

    def store_stats(self):
        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            f"**{', '.join(self.store_type)} for sale:"
        ]

        products: dict[str, dict] = {}
        for product in self.products:
            key = product.model
            if key not in products:
                products[key] = {"pieces": 0, "total_price": 0}
            products[key]["pieces"] += 1
            products[key]["total_price"] += product.price

        for model in sorted(products.keys()):
            count = products[model]["pieces"]
            avg_price = products[model]["total_price"] / count
            result.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return "\n".join(result)
