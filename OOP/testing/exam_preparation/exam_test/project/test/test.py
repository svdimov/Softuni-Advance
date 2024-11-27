from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class SoccerPlayerTest(TestCase):
    def setUp(self):
        self.p = SoccerPlayer('TestTest', 17, 2, "Barcelona")

    def test_init(self):
        p = SoccerPlayer('TestTest', 16, 2, "Barcelona")

        self.assertEqual(self.p.name, "TestTest")
        self.assertEqual(self.p.age, 16)
        self.assertEqual(self.p.goals, 2)
        self.assertEqual(self.p.team, "Barcelona")
        self.assertEqual(self.p.achievements, {})

        self.assertEqual(SoccerPlayer._VALID_TEAMS,
                         ["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"])

    def test_name_invalid_name_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.p.name = 'Test5'
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

        with self.assertRaises(ValueError) as ex:
            self.p.name = 'Test'
        self.assertEqual(str(ex.exception), "Name should be more than 5 symbols!")

    def test_age_invalid_age_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.p.age = 15
        self.assertEqual(str(ex.exception), "Players must be at least 16 years of age!")

    def test_goal_are_negative_sets_to_zero(self):
        self.p.goals = -1
        self.assertEqual(self.p.goals, 0)

    def test_invalid_team_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.p.team = "Invalid"
        valid_teams = SoccerPlayer._VALID_TEAMS
        self.assertEqual(str(ex.exception), f"Team must be one of the following: {', '.join(valid_teams)}!")

    def test_change_team_invalid_team(self):
        self.assertEqual(self.p.team, "Barcelona")
        result = self.p.change_team("Invalid")
        self.assertEqual(result, "Invalid team name!")

        self.assertEqual(self.p.team, "Barcelona")

    def test_change_team_valid_name(self):
        self.assertEqual(self.p.team, "Barcelona")
        result = self.p.change_team("Real Madrid")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.p.team, "Real Madrid")

    def test_add_increment_new_achievements(self):
        self.assertEqual(self.p.achievements, {})

        result = self.p.add_new_achievement("Test")
        self.assertEqual(result, f"{'Test'} has been successfully added to the achievements collection!")

        self.assertEqual(self.p.achievements, {'Test': 1})

        result = self.p.add_new_achievement('Test')
        self.assertEqual(result, f"{'Test'} has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {'Test': 2})
        # add new achievement
        result = self.p.add_new_achievement('Test2')
        self.assertEqual(result, f"{'Test2'} has been successfully added to the achievements collection!")
        self.assertEqual(self.p.achievements, {'Test': 2, 'Test2': 1})

    def test_comparison(self):

        p2 = SoccerPlayer('TestTest2', 18, 1, "Manchester United")

        result = self.p < p2
        self.assertEqual(result, f"{self.p.name} is a better goal scorer than {p2.name}.")

        result = p2 > self.p
        self.assertEqual(result, f"{self.p.name} is a better goal scorer than {p2.name}.")


        p2.goals = 2
        result = p2 < self.p
        self.assertEqual(result, f"{p2.name} is a better goal scorer than {self.p.name}.")
        # test considered
        p2.goals = 2
        result = self.p < p2
        self.assertEqual(result, f"{self.p.name} is a better goal scorer than {p2.name}.")

        self.p.goals = 1
        self.assertLess(self.p.goals, p2.goals)
        result = self.p < p2
        self.assertEqual(result, f"{p2.name} is a top goal scorer! S/he scored more than {self.p.name}.")

    def test_comparison_equal_players_goals(self):
        p2 = SoccerPlayer('TestTest2', 18, 2, "Manchester United")
        with self.assertRaises(TypeError):
            result = self.p <= p2


if __name__ == '__main__':
    main()
