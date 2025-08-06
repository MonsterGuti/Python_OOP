from products.base_product import BaseProduct
from products.chair import Chair
from products.hobby_horse import HobbyHorse
from stores.base_store import BaseStore
from stores.furniture_store import FurnitureStore
from stores.toy_store import ToyStore


class FactoryManager:
    product_types: dict[str, type[BaseProduct]] = {
        "Chair": Chair,
        "HobbyHorse": HobbyHorse
    }

    store_types: dict[str, type[BaseStore]] = {
        "FurnitureStore": FurnitureStore,
        "ToyStore": ToyStore
    }

    def __init__(self, name: str):
        self.name = name
        self.income = 0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.product_types:
            raise ValueError("Invalid product type!")
        product = self.product_types[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.store_types:
            raise ValueError(f"{store_type} is an invalid type of stores!")
        new_store = self.store_types[store_type](name, location)
        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            raise ValueError(f"Store {store.name} has no capacity for this purchase.")

        filtered_products = [p for p in products if p.sub_type in store.store_type]

        if not filtered_products:
            return "Products do not match in type. Nothing sold."

        for product in filtered_products:
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price
            store.products.append(product)

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such stores!")

        if store.products:
            return "The stores is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered stores {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        filtered_products = [p for p in self.products if p.model == product_model]
        for product in filtered_products:
            product.discount()
        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no stores registered under this name!"
        return store.store_stats()

    def statistics(self):
        products_count: dict[str, int] = {}
        total_price = 0
        for p in self.products:
            products_count[p.model] = products_count.get(p.model, 0) + 1
            total_price += p.price

        unsold_names = [p.model for p in self.products]

        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(unsold_names)}. Total net price: {total_price:.2f}",
        ]

        for product_model, count in sorted(products_count.items()):
            result.append(f"{product_model}: {count}")

        result.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            result.append(store.name)

        return "\n".join(result)
