from unittest import TestCase, main
from project.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Arthur", 10, 100.0, 15.0)
        self.enemy = Hero("Lancelot", 8, 80.0, 10.0)

    def test_initialization(self):
        self.assertEqual(self.hero.username, "Arthur")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 100.0)
        self.assertEqual(self.hero.damage, 15.0)

    def test_battle_with_self_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_with_zero_or_negative_health_raises(self):
        bad_health = [0, -10]
        for health in bad_health:
            self.hero.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_with_zero_or_negative_health_raises(self):
        bad_health = [0, -10]
        for health in bad_health:
            self.enemy.health = health
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(str(ex.exception), f"You cannot fight {self.enemy.username}. He needs to rest")

    def test_battle_draw(self):
        # Setup both to die simultaneously
        self.hero.health = 80
        self.hero.damage = 10
        self.hero.level = 8

        self.enemy.health = 80
        self.enemy.damage = 10
        self.enemy.level = 8

        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "Draw")
        self.assertEqual(self.hero.health, 0)
        self.assertEqual(self.enemy.health, 0)

    def test_battle_hero_wins(self):
        self.enemy.health = 50  # low enough for hero to win

        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 11)
        expected_hero_health = 100.0 - (self.enemy.damage * self.enemy.level) + 5
        self.assertEqual(self.hero.health, expected_hero_health)
        self.assertEqual(self.hero.damage, 15.0 + 5)

    def test_battle_hero_loses(self):
        self.hero.health = 50
        self.hero.damage = 5.0
        self.hero.level = 5

        self.enemy.health = 150
        self.enemy.damage = 15.0
        self.enemy.level = 10

        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(self.enemy.level, 11)
        expected_enemy_health = 150 - (self.hero.damage * self.hero.level) + 5
        self.assertEqual(self.enemy.health, expected_enemy_health)
        self.assertEqual(self.enemy.damage, 15.0 + 5)

    def test_hero_str(self):
        expected = "Hero Arthur: 10 lvl\nHealth: 100.0\nDamage: 15.0\n"
        self.assertEqual(str(self.hero), expected)

if __name__ == '__main__':
    main()
