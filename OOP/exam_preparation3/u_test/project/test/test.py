from unittest import TestCase,main
from project.restaurant import Restaurant



class TestRestaurant(TestCase):

    def setUp(self):
        self.r = Restaurant("Testaurant", 5)


    def test_init(self):
        self.assertEqual([],self.r.waiters)
        self.assertEqual(5,self.r.capacity)
        self.assertEqual('Testaurant',self.r.name)

    def test_name_property(self):
        # Valid name
        self.r.name = "Valid Name"
        self.assertEqual(self.r.name, "Valid Name")

        # Invalid name
        with self.assertRaises(ValueError):
            self.r.name = "   "
        with self.assertRaises(ValueError):
            self.r.name = ""

    def test_capacity_property(self):
        # Valid capacity
        self.r.capacity = 10
        self.assertEqual(self.r.capacity, 10)

        # Invalid capacity
        with self.assertRaises(ValueError):
            self.r.capacity = -5

    def test_add_waiter(self):
        result = self.r.add_waiter("John")
        self.assertEqual(result, "The waiter John has been added.")
        self.assertEqual(len(self.r.waiters), 1)

        # Adding the same waiter
        result = self.r.add_waiter("John")
        self.assertEqual(result, "The waiter John already exists!")
        self.assertEqual(len(self.r.waiters), 1)

        # Adding waiters up to capacity
        self.r.add_waiter("Jane")
        self.r.add_waiter("Alice")
        self.r.add_waiter("Bob")
        self.r.add_waiter("Charlie")
        result = self.r.add_waiter("Dave")
        self.assertEqual(result, "No more places!")

    def test_remove_waiter(self):
        self.r.add_waiter("John")
        self.r.add_waiter("Jane")

        # Removing an existing waiter
        result = self.r.remove_waiter("John")
        self.assertEqual(result, "The waiter John has been removed.")
        self.assertEqual(len(self.r.waiters), 1)

        # Removing a non-existing waiter
        result = self.r.remove_waiter("John")
        self.assertEqual(result, "No waiter found with the name John.")

    def test_get_waiters(self):
        # Adding waiters with earnings
        self.r.waiters = [
            {'name': 'John', 'total_earnings': 500},
            {'name': 'Jane', 'total_earnings': 300},
            {'name': 'Alice', 'total_earnings': 700},
        ]

        # Filtering by minimum earnings
        waiters_min_earnings = self.r.get_waiters(min_earnings=400)
        self.assertEqual(len(waiters_min_earnings), 2)
        self.assertIn({'name': 'John', 'total_earnings': 500}, waiters_min_earnings)
        self.assertIn({'name': 'Alice', 'total_earnings': 700}, waiters_min_earnings)

        # Filtering by maximum earnings
        waiters_max_earnings = self.r.get_waiters(max_earnings=400)
        self.assertEqual(len(waiters_max_earnings), 1)
        self.assertIn({'name': 'Jane', 'total_earnings': 300}, waiters_max_earnings)

        # Filtering by range
        waiters_range = self.r.get_waiters(min_earnings=400, max_earnings=600)
        self.assertEqual(len(waiters_range), 1)
        self.assertIn({'name': 'John', 'total_earnings': 500}, waiters_range)

    def test_get_total_earnings(self):
        # Adding waiters with earnings
        self.r.waiters = [
            {'name': 'John', 'total_earnings': 500},
            {'name': 'Jane', 'total_earnings': 300},
            {'name': 'Alice', 'total_earnings': 700},
        ]
        self.assertEqual(self.r.get_total_earnings(), 1500)

        # No waiters
        self.r.waiters = []
        self.assertEqual(self.r.get_total_earnings(), 0)

if __name__ == "__main__":
    main()


