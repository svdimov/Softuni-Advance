from project.vehicle import Vehicle
from unittest import TestCase,main
class VehicleTest(TestCase):
    fuel = 3.5
    horse_power = 100.0

    def setUp(self):
        self.test_vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.test_vehicle.fuel)
        self.assertEqual(self.fuel, self.test_vehicle.capacity)
        self.assertEqual(self.horse_power, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_class_attributes(self):
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)
        self.assertIsInstance(self.test_vehicle.DEFAULT_FUEL_CONSUMPTION, float)

    def test_drive_success(self):
        self.test_vehicle.drive(2)
        self.assertEqual(self.test_vehicle.fuel, 1)

    def test_drive_grater_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(5)
        self.assertEqual(str(ex.exception),"Not enough fuel")


    def test_refuel_success(self):
        self.test_vehicle.fuel = 1
        self.test_vehicle.refuel(1.2)
        self.assertEqual(self.test_vehicle.fuel, 2.2)

    def test_refuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.refuel(9)
        self.assertEqual(str(ex.exception),"Too much fuel")

    def test_str(self):
        expected = "The vehicle has 100.0 horse power with 3.5 fuel left and 1.25 fuel consumption"


        self.assertEqual(expected, str(self.test_vehicle))



if __name__ == '__main__':
    main()