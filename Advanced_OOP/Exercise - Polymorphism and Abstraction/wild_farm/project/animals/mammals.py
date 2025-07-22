from abc import ABC
from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat

class Mouse(Mammal, ABC):
    WEIGHT_GAIN = 0.10
    ALLOWED_FOOD = [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"

    def eat(self, food):
        if type(food) not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity
        return None


class Dog(Mammal, ABC):
    WEIGHT_GAIN = 0.40
    ALLOWED_FOOD = [Meat]

    def make_sound(self):
        return "Woof!"

    def eat(self, food):
        if type(food) not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity
        return None


class Cat(Mammal, ABC):
    WEIGHT_GAIN = 0.30
    ALLOWED_FOOD = [Vegetable, Meat]

    def make_sound(self):
        return "Meow"

    def eat(self, food):
        if type(food) not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity
        return None


class Tiger(Mammal, ABC):
    WEIGHT_GAIN = 1.00
    ALLOWED_FOOD = [Meat]

    def make_sound(self):
        return "ROAR!!!"

    def eat(self, food):
        if type(food) not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity
        return None
