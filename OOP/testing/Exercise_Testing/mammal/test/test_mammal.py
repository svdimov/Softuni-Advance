from project.mammal import Mammal

from unittest import  TestCase, main

class MammalTest(TestCase):

    def test_init(self):
        m = Mammal('sharo','dog','woof')
        self.assertEqual(m.name,'sharo')
        self.assertEqual(m.type,'dog')
        self.assertEqual(m.sound,'woof')
        # self.assertEqual(m.get_kingdom(),'animals')
        self.assertEqual(m._Mammal__kingdom,'animals')

    def test_make_sound(self):
        m = Mammal('sharo', 'dog', 'woof')
        result = m.make_sound()
        expected = f"{m.name} makes {m.sound}"
        self.assertEqual(expected,result)

    def test_get_kingdom(self):
        m = Mammal('sharo', 'dog', 'woof')
        result = m.get_kingdom()
        expected = 'animals'
        self.assertEqual(expected,result)

    def test_info(self):
        m = Mammal('sharo', 'dog', 'woof')
        result = m.info()
        expected  = f"{m.name} is of type {m.type}"

        self.assertEqual(expected,result)


if __name__ == '__main__':
    main()