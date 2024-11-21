from lab.test_cat import Cat
from unittest import TestCase,main

class TestCat(TestCase):
    def test_init(self):
        c = Cat('Kleo')
        self.assertEqual(c.name,'Kleo')
        self.assertFalse(c.fed)
        # self.assertFalse(c.fed) same like self.assertEqual(c.fed,False)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size,0)


    def test_eat(self):

        c = Cat('Kleo')

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

        result = c.eat()
        self.assertIsNone(result)

        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size, 1)


    def test_cat_not_eat_raises(self):
        c = Cat('Kleo')
        c.eat()
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size,1)
        #ACT
        with self.assertRaises(Exception) as ex:
            c.eat()
        #ASSERT
        self.assertEqual(str(ex.exception),'Already fed.')
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size,1)

    def test_sleep_cat_not_fed_raises(self):
        c = Cat('Klep')

        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)

        with self.assertRaises(Exception) as ex:
            c.sleep()

        self.assertEqual(str(ex.exception),'Cannot sleep while hungry')
        self.assertFalse(c.sleepy)

    def test_cat_sleeps(self):
        c = Cat('Kleo')
        c.eat()
        self.assertTrue(c.sleepy)

        c.sleep()
        self.assertFalse(c.sleepy)


if __name__ == '__main__':
    main()
