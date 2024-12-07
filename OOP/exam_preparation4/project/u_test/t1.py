
import unittest

class TestTennisPlayer(unittest.TestCase):
    def setUp(self):
        """Set up a common test environment."""
        self.player1 = TennisPlayer(name="Serena", age=30, points=8500.5)
        self.player2 = TennisPlayer(name="Roger", age=35, points=9000.3)

    def test_initialization(self):
        """Test that TennisPlayer initializes correctly."""
        self.assertEqual(self.player1.name, "Serena")
        self.assertEqual(self.player1.age, 30)
        self.assertEqual(self.player1.points, 8500.5)
        self.assertEqual(self.player1.wins, [])

    def test_name_validation(self):
        """Test name validation."""
        with self.assertRaises(ValueError) as ex:
            self.player1.name = "A"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_age_validation(self):
        """Test age validation."""
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_new_win(self):
        """Test adding new wins."""
        self.player1.add_new_win("US Open")
        self.assertIn("US Open", self.player1.wins)

        response = self.player1.add_new_win("US Open")
        self.assertEqual(response, "US Open has been already added to the list of wins!")

    def test_lt_operator(self):
        """Test the < operator comparison."""
        result1 = self.player1 < self.player2
        self.assertEqual(result1, "Roger is a top seeded player and he/she is better than Serena")

        result2 = self.player2 < self.player1
        self.assertEqual(result2, "Roger is a better player than Serena")

    def test_str_representation(self):
        """Test the string representation of TennisPlayer."""
        self.player1.add_new_win("Wimbledon")
        player_str = str(self.player1)
        expected_str = (
            "Tennis Player: Serena\n"
            "Age: 30\n"
            "Points: 8500.5\n"
            "Tournaments won: Wimbledon"
        )
        self.assertEqual(player_str, expected_str)

if __name__ == '__main__':
    unittest.main()
