from project.tennis_player import TennisPlayer
from unittest import TestCase,main

class TestTennisPlayer(TestCase):
    def setUp(self):
        """Set up the test environment with example players."""
        self.player1 = TennisPlayer(name="Serena", age=30, points=8500.5)
        self.player2 = TennisPlayer(name="Roger", age=35, points=9000.3)

    def test_initialization(self):
        """Test proper initialization of TennisPlayer."""
        # Check attribute values
        self.assertEqual(self.player1.name, "Serena", "Player1 name mismatch")
        self.assertEqual(self.player1.age, 30, "Player1 age mismatch")
        self.assertEqual(self.player1.points, 8500.5, "Player1 points mismatch")
        self.assertListEqual(self.player1.wins, [], "Player1 wins list should be empty initially")

        # Test initialization for a different player
        self.assertEqual(self.player2.name, "Roger", "Player2 name mismatch")
        self.assertEqual(self.player2.age, 35, "Player2 age mismatch")
        self.assertEqual(self.player2.points, 9000.3, "Player2 points mismatch")

    def test_name_validation(self):
        """Test validation of the name property."""
        # Valid name
        self.player1.name = "Venus"
        self.assertEqual(self.player1.name, "Venus", "Name should be updated to Venus")

        # Invalid name
        with self.assertRaises(ValueError) as ex:
            self.player1.name = "A"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

        # Ensure name remains unchanged after invalid assignment
        self.assertEqual(self.player1.name, "Venus", "Name should remain as Venus after invalid assignment")

    def test_age_validation(self):
        """Test validation of the age property."""
        # Valid age
        self.player1.age = 25
        self.assertEqual(self.player1.age, 25, "Age should be updated to 25")

        # Invalid age
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

        # Ensure age remains unchanged after invalid assignment
        self.assertEqual(self.player1.age, 25, "Age should remain as 25 after invalid assignment")

    def test_add_new_win(self):
        """Test adding new tournament wins."""
        # Add a valid win
        self.player1.add_new_win("US Open")
        self.assertIn("US Open", self.player1.wins, "US Open should be in the wins list")

        # Add another win
        self.player1.add_new_win("Wimbledon")
        self.assertIn("Wimbledon", self.player1.wins, "Wimbledon should be in the wins list")
        self.assertEqual(len(self.player1.wins), 2, "Wins list should contain exactly 2 tournaments")

        # Add a duplicate win
        response = self.player1.add_new_win("US Open")
        self.assertEqual(response, "US Open has been already added to the list of wins!", "Duplicate win message mismatch")
        self.assertEqual(len(self.player1.wins), 2, "Wins list should still contain only unique tournaments")

    def test_lt_operator(self):
        """Test the behavior of the < operator."""
        # Compare players based on points
        result1 = self.player1 < self.player2
        self.assertEqual(result1, "Roger is a top seeded player and he/she is better than Serena", "Comparison result mismatch when Player1 has fewer points")

        result2 = self.player2 < self.player1
        self.assertEqual(result2, "Roger is a better player than Serena", "Comparison result mismatch when Player2 has more points")

        # Test players with equal points
        self.player1.points = 9000.3
        result3 = self.player1 < self.player2
        self.assertEqual(result3, "Serena is a better player than Roger", "Comparison result mismatch for players with equal points")

    def test_str_representation(self):
        """Test the string representation of TennisPlayer."""
        # Without wins
        expected_str_no_wins = (
            "Tennis Player: Serena\n"
            "Age: 30\n"
            "Points: 8500.5\n"
            "Tournaments won: "
        )
        self.assertEqual(str(self.player1), expected_str_no_wins, "String representation mismatch when no tournaments won")

        # With wins
        self.player1.add_new_win("Australian Open")
        self.player1.add_new_win("French Open")
        expected_str_with_wins = (
            "Tennis Player: Serena\n"
            "Age: 30\n"
            "Points: 8500.5\n"
            "Tournaments won: Australian Open, French Open"
        )
        self.assertEqual(str(self.player1), expected_str_with_wins, "String representation mismatch with tournaments won")

    def test_edge_cases(self):
        """Test edge cases for properties and methods."""
        # Edge case for name length
        with self.assertRaises(ValueError):
            self.player1.name = "Ed"

        # Edge case for minimum valid age
        self.player1.age = 18
        self.assertEqual(self.player1.age, 18, "Minimum valid age assignment failed")

        # Edge case for 0 wins
        self.assertEqual(self.player1.wins, [], "Wins list should be empty initially")

        # Adding and validating a large number of wins
        for i in range(100):
            self.player1.add_new_win(f"Tournament {i}")
        self.assertEqual(len(self.player1.wins), 100, "Wins list should contain 100 unique tournaments")

if __name__ == '__main__':
    main()
