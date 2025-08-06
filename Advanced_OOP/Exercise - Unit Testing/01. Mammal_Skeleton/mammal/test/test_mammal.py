from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Leo", "Lion", "Roar")

    def test_init_mammal(self):
        self.assertEqual(self.mammal.name, "Leo")
        self.assertEqual(self.mammal.type, "Lion")
        self.assertEqual(self.mammal.sound, "Roar")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Leo makes Roar")

    def test_mammal_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_mammal_info(self):
        self.assertEqual(self.mammal.info(), "Leo is of type Lion")




if __name__ == "__main__":
    main()