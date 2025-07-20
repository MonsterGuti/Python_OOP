from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_FUEL_USAGE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.SUMMER_FUEL_USAGE) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_FUEL_USAGE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.SUMMER_FUEL_USAGE) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)  # Очаквано: 100 - (15+1.6)*5 = 100 - 83 = 17.0
truck.refuel(50)
print(truck.fuel_quantity)  # Очаквано: 17.0 + (50*0.95) = 17 + 47.5 = 64.5
