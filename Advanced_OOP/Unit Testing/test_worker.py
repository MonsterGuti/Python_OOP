

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase
import unittest

class WorkerTest(TestCase):
    def setUp(self):
        self.worker = Worker("John", 100, 10)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_increases_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_worker_throws_exception_when_energy_is_0_or_less(self):
        worker_zero_energy = Worker("Bob", 50, 0)
        with self.assertRaises(Exception) as ex:
            worker_zero_energy.work()
        self.assertEqual(str(ex.exception), "Not enough energy.")

        worker_negative_energy = Worker("Alice", 50, -1)
        with self.assertRaises(Exception) as ex:
            worker_negative_energy.work()
        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_worker_money_increases_correctly_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_worker_energy_decreases_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info_returns_correct_string(self):
        self.assertEqual(self.worker.get_info(), "John has saved 0 money.")
        self.worker.work()
        self.assertEqual(self.worker.get_info(), "John has saved 100 money.")

if __name__ == '__main__':
    unittest.main()
