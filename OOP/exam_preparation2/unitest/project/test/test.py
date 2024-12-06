from project.furniture import Furniture
from unittest import TestCase, main


class FurnitureTest(TestCase):
    def setUp(self):
        self.f = Furniture('test', 100, (10, 10, 10))

    def test_init_by_default(self):
        self.assertEqual('test', self.f.model)
        self.assertEqual(100, self.f.price)
        self.assertEqual((10, 10, 10), self.f.dimensions)
        self.assertTrue(self.f.in_stock)
        self.assertIsNone(self.f.weight)

    def test_init_passed_values(self):
        f = Furniture('test', 100, (10, 10, 10), False, 99)
        self.assertEqual('test', f.model)
        self.assertEqual(100, f.price)
        self.assertEqual((10, 10, 10), f.dimensions)
        self.assertFalse(f.in_stock)
        self.assertEqual(99, f.weight)

    def test_model_whitespaces_only_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.f.model = ""
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.f.model = "    "
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_model_greater_50_chars(self):
        with self.assertRaises(ValueError) as ex:
            self.f.model = "a" * 51
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_price_negative_number_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.f.price = -1
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_dimension_exact_3_character_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = 10, 10, 10, 10
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

    def test_dimension_negative_integer_value_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = 0, -2, 3
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_wight_value_is_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.f.weight = 0
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_wight_negative_number(self):
        with self.assertRaises(ValueError) as ex:
            self.f.weight = -1
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_get_available_status_in_stock(self):
        self.assertTrue(self.f.in_stock)

        result = self.f.get_available_status()
        self.assertEqual('Model: test is currently in stock.',result)
    def test_get_available_status_not_in_stock(self):
        self.f.in_stock = False
        self.assertFalse(self.f.in_stock)

        result = self.f.get_available_status()
        self.assertEqual("Model: test is currently unavailable.",result)

    def test_get_specifications_no_weight(self):
        self.assertIsNone(self.f.weight)
        result = self.f.get_specifications()
        self.assertEqual((f"Model: {self.f.model}"
                          f" has the following dimensions: "
                          f"{self.f.dimensions[0]}mm x {self.f.dimensions[1]}mm x {self.f.dimensions[2]}mm "
                          f"and weighs: N/A"),
                         result)

    def test_get_specifications_with_weight(self):
        self.f.weight = 50
        self.assertEqual(50,self.f.weight)
        result = self.f.get_specifications()
        self.assertEqual((f"Model: {self.f.model}"
                          f" has the following dimensions: "
                          f"{self.f.dimensions[0]}mm x {self.f.dimensions[1]}mm x {self.f.dimensions[2]}mm "
                          f"and weighs: {self.f.weight}"),
                         result)






if __name__ == '__main__':
    main()
