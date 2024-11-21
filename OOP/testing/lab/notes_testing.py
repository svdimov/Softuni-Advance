from unittest import TestCase
def sum_nums(a,b):
    return a + b

class SumTest(TestCase):

    def test_sum_nums_return_result(self):
        expected_result = 10

        # Act
        actual_result = sum_nums(5,6)

        # Assert
        self.assertEqual(actual_result,expected_result)



