

from project.hero import Hero
from unittest import TestCase, main

class HeroTest(TestCase):

    def setUp(self):
        self.hero = Hero('Stefan',5,39.5,15.3)

    def test_init(self):
        self.assertEqual(self.hero.username,'Stefan')
        self.assertEqual(self.hero.level,5)
        self.assertEqual(self.hero.health,39.5)
        self.assertEqual(self.hero.damage,15.3)

    def test_attributes(self):
        self.assertIsInstance(self.hero.username,str)
        self.assertIsInstance(self.hero.level,int)
        self.assertIsInstance(self.hero.health,float)
        self.assertIsInstance(self.hero.damage,float)

    def test_battle_error_equal_username(self):
        enemy_hero = Hero('Stefan',5,39.5,25.0)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception),"You cannot fight yourself")

    def test_battle_health_is_negative_or_zero(self):
        self.hero.health = 0
        enemy_hero = Hero('Gosho', 2, 90.0, 15.3)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception),"Your health is lower than or equal to 0. You need to rest")
        self.hero.health = -1
        enemy_hero = Hero('Gosho', 2, 90.0, 25.0)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")
    def test_battle_enemy_hero_is_zero_or_negative(self):

        enemy_hero = Hero('Gosho', 2, 0.0, 25.0)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception),f"You cannot fight {enemy_hero.username}. He needs to rest")

        enemy_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), f"You cannot fight {enemy_hero.username}. He needs to rest")
    def test_battle_draw(self):
        enemy_hero = Hero('Gosho', 5, 39.5, 15.3)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.level,5)
        self.assertEqual(self.hero.health,-37)
        self.assertEqual(self.hero.damage,15.3)
        self.assertEqual("Draw",result)
    def test_battle_hero_win(self):
        enemy_hero = Hero('Gosho',1,1,1)
        result = self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.level,6)
        self.assertEqual(self.hero.health,43.5)
        self.assertEqual(self.hero.damage,20.3)
        self.assertEqual(result,"You win")

    def test_battle_hero_lose(self):
        enemy_hero = Hero('Gosho', 100, 100, 100)

        result = self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.level,5)
        self.assertEqual(self.hero.health,-9960.5)
        self.assertEqual(self.hero.damage,15.3)
        self.assertEqual(result,"You lose")


        self.assertEqual(101,enemy_hero.level)
        self.assertEqual(28.5,enemy_hero.health)
        self.assertEqual(105,enemy_hero.damage)


    def test_str(self):
        expected =  f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(str(self.hero),expected)


if __name__ == '__main__':
    main()
