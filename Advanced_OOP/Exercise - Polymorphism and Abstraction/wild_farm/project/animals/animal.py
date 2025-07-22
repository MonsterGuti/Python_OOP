from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        return self.eat(food)

    @abstractmethod
    def eat(self, food):
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        # Format weight without trailing zeros on decimals:
        w = int(self.weight) if self.weight.is_integer() else self.weight
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {w}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        w = int(self.weight) if self.weight.is_integer() else self.weight
        return f"{self.__class__.__name__} [{self.name}, {w}, {self.living_region}, {self.food_eaten}]"
