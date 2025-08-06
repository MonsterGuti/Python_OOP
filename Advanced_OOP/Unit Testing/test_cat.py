class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


import unittest
from unittest import TestCase

class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Ema")

    def test_cat_size_increases_after_eating(self):
        self.assertEqual(self.cat.size, 0)
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_cat_cannot_eat_if_already_fed_raises(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual(str(ex.exception), "Already fed.")

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), "Cannot sleep while hungry")

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == "__main__":
    unittest.main()


