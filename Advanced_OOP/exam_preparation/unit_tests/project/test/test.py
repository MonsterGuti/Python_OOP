from project.soccer_player import SoccerPlayer
import unittest


class TestSoccerPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = SoccerPlayer("Lionel Messi", 34, 700, "Barcelona")
        self.player2 = SoccerPlayer("Cristiano Ronaldo", 36, 750, "Juventus")

    def test_initialization(self):
        self.assertEqual(self.player1.name, "Lionel Messi")
        self.assertEqual(self.player1.age, 34)
        self.assertEqual(self.player1.goals, 700)
        self.assertEqual(self.player1.team, "Barcelona")
        self.assertEqual(self.player1.achievements, {})

    def test_name_validation(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.name = "Messi"
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_age_validation(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 15
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_goals_validation(self):
        self.player1.goals = -1
        self.assertEqual(self.player1.goals, 0)

    def test_team_validation(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.team = "Unknown Team"
        self.assertEqual(str(ex.exception), "Team must be one of the following: Barcelona, Real Madrid, "
                                            "Manchester United, Juventus, PSG!")

    def test_change_team__valid_name(self):
        result = self.player1.change_team("PSG")
        self.assertEqual(self.player1.team, "PSG")
        self.assertEqual(result, "Team successfully changed!")

    def test_change_team__invalid_name(self):
        result = self.player1.change_team("Unknown Team")
        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.player1.team, "Barcelona")

    def test_add_new_achievement__not_existing(self):
        result = self.player1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.player1.achievements), 1)

    def test_add_new_achievement__twice(self):
        result = self.player1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.player1.achievements), 1)

        result = self.player1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements["Ballon d'Or"], 2)
        self.assertEqual(len(self.player1.achievements), 1)

    def test_add_new_achievement__two_different(self):
        result = self.player1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.player1.achievements), 1)

        result = self.player1.add_new_achievement("Champions League")
        self.assertEqual(result, "Champions League has been successfully added to the achievements collection!")
        self.assertEqual(self.player1.achievements["Champions League"], 1)
        self.assertEqual(len(self.player1.achievements), 2)

    def test_comparison(self):
        self.assertEqual(self.player1 < self.player2, 'Cristiano Ronaldo is a top goal scorer! S/he scored more than '
                                                      'Lionel Messi.')
        self.assertEqual(self.player2 < self.player1, 'Cristiano Ronaldo is a better goal scorer than Lionel Messi.')


if __name__ == '__main__':
    unittest.main()
