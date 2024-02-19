import unittest

from firearm.bullet import Bullet
from firearm.gun import Gun


class TestGun(unittest.TestCase):

    def setUp(self):
        self.pistol = Gun("Pistol", "Glock", 10, "9mm")

    def test_loadTen9mmBulletsIntoTheMagazine_NumberOfBulletsIsTen(self):
        bullets = []
        for count in range(10):
            bullets.append(Bullet("9mm"))
        print(f"\n{bullets}")
        self.pistol.load_magazine(bullets)

        self.assertEqual(10, self.pistol.number_of_bullets())

    def test_loadZero9mmBulletsIntoTheMagazine_NumberOfBulletsIsZero(self):
        bullets = []
        self.pistol.load_magazine(bullets)

        self.assertEqual(0, self.pistol.number_of_bullets())

    def test_loadElevwn9mmBulletsIntoTheMagazine_NumberOfBulletsIsTen(self):
        bullets = []
        for count in range(10):
            bullets.append(Bullet("9mm"))
        print(f"\n{bullets}")
        self.pistol.load_magazine(bullets)

        self.assertEqual(10, self.pistol.number_of_bullets())


