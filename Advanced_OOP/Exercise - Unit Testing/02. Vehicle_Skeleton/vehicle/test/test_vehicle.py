from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 200)

    def test_init_vehicle(self):
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.capacity, 100)
        self.assertEqual(self.vehicle.horse_power, 200)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_vehicle_valid(self):
        self.vehicle.drive(20)
        self.assertEqual(self.vehicle.fuel, 75)

    def test_drive_vehicle_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_refuel_vehicle_valid(self):
        self.vehicle.drive(40)
        self.vehicle.refuel(30)
        self.assertEqual(self.vehicle.fuel, 80)

    def test_refuel_vehicle_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_str_returns_proper_string(self):
        result = str(self.vehicle)
        expected = "The vehicle has 200 horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
