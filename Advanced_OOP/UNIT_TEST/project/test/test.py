from project.legendary_item import LegendaryItem

from unittest import main, TestCase


class TestLegendaryItem(TestCase):
    def setUp(self):
        self.item = LegendaryItem("TEST-123", power=30, durability=90, price=60)

    def test_init_properties(self):
        self.assertEqual(self.item.identifier, "TEST-123")
        self.assertEqual(self.item.power, 30)
        self.assertEqual(self.item.durability, 90)
        self.assertEqual(self.item.price, 60)

    def test_identifier_invalid_chars(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("AB!", power=30, durability=90, price=60)
        self.assertEqual(str(ex.exception), "Identifier can only contain letters, digits, or hyphens!")

    def test_identifier_too_short(self):
        with self.assertRaises(ValueError) as ex:
            LegendaryItem("ABC", power=30, durability=90, price=60)
        self.assertEqual(str(ex.exception), "Identifier must be at least 4 characters long!")

    def test_power_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.item = LegendaryItem("TEST-123", power=-30, durability=90, price=60)
        self.assertEqual(str(ex.exception), "Power must be a non-negative integer!")

    def test_durability_too_low(self):
        with self.assertRaises(ValueError) as ex:
            self.item = LegendaryItem("TEST-123", power=30, durability= -90, price=60)
        self.assertEqual(str(ex.exception), "Durability must be between 1 and 100 inclusive!")

    def test_durability_too_high(self):
        with self.assertRaises(ValueError) as ex:
            self.item = LegendaryItem("TEST-123", power=30, durability=190, price=60)
        self.assertEqual(str(ex.exception), "Durability must be between 1 and 100 inclusive!")

    def test_price_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.item = LegendaryItem("TEST-123", power=30, durability=90, price=0)
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

    def test_price_not_multiple_of_10(self):
        with self.assertRaises(ValueError) as ex:
            self.item = LegendaryItem("TEST-123", power=30, durability=90, price=3)
        self.assertEqual(str(ex.exception), "Price must be a multiple of 10 and not 0!")

    def test_is_precious_true(self):
        self.item.power = 50
        self.assertTrue(self.item.is_precious)
        self.item.power = 100
        self.assertTrue(self.item.is_precious)

    def test_is_precious_false(self):
        self.item.power = 49
        self.assertFalse(self.item.is_precious)

    def test_enhance_increases_power_price_and_durability(self):
        self.item.power = 10
        self.item.price = 30
        self.item.durability = 75
        self.item.enhance()
        self.assertEqual(self.item.power, 20)
        self.assertEqual(self.item.price, 40)
        self.assertEqual(self.item.durability, 85)

    def test_enhance_increases_power_price_and_durability_with_higher_durability(self):
        self.item.power = 10
        self.item.price = 30
        self.item.durability = 95
        self.item.enhance()
        self.assertEqual(self.item.power, 20)
        self.assertEqual(self.item.price, 40)
        self.assertEqual(self.item.durability, 100)

    def test_evaluate_eligible(self):
        self.item.power = 51
        self.item.durability = 80
        result = self.item.evaluate(70)
        self.assertEqual(result, f"{self.item.identifier} is eligible.")

    def test_evaluate_not_eligible_low_durability(self):
        self.item.power = 60
        self.item.durability = 50
        result = self.item.evaluate(60)
        self.assertEqual(result, "Item not eligible.")

    def test_evaluate_not_eligible_not_precious(self):
        self.item.power = 49
        self.item.durability = 65
        result = self.item.evaluate(60)
        self.assertEqual(result, "Item not eligible.")

if __name__ == "__main__":
    main()

