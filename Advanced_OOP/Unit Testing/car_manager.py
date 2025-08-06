class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)

import unittest
from unittest import TestCase


class CarTest(TestCase):
    def setUp(self):
        self.car = Car("Mercedes", "CLK", 10, 60)

    def test_initialization_sets_all_properties_correctly(self):
        self.assertEqual(self.car.make, "Mercedes")
        self.assertEqual(self.car.model, "CLK")
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_setter_raises_if_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_setter_raises_if_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_setter_raises_if_zero_or_negative(self):
        for value in [0, -5]:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_consumption = value
            self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_setter_raises_if_zero_or_negative(self):
        for value in [0, -10]:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_capacity = value
            self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_setter_raises_if_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_adds_fuel_when_valid(self):
        self.car.refuel(30)
        self.assertEqual(self.car.fuel_amount, 30)

    def test_refuel_caps_at_fuel_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_raises_when_zero_or_negative(self):
        for value in [-1, 0]:
            with self.assertRaises(Exception) as ex:
                self.car.refuel(value)
            self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_reduces_fuel_amount_correctly(self):
        self.car.refuel(60)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_drive_raises_if_not_enough_fuel(self):
        self.car.refuel(5)
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

if __name__ == "__main__":
    unittest.main()