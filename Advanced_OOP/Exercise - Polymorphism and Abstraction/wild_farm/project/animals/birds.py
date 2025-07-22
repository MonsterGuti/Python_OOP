from abc import ABC
from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed

class Owl(Bird, ABC):
    WEIGHT_GAIN = 0.25
    ALLOWED_FOOD = [Meat]

    def make_sound(self):
        return "Hoot Hoot"

    def eat(self, food):
        if type(food) not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity
        return None


class Hen(Bird, ABC):
    WEIGHT_GAIN = 0.35
    ALLOWED_FOOD = [Vegetable, Fruit, Meat, Seed]

    def make_sound(self):
        return "Cluck"

    def eat(self, food):
        # Hen eats everything, so no restriction here
        if type(food) not in self.ALLOWED_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity
        return None
