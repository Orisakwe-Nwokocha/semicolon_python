import unittest

from firearm.bullet import Bullet
from firearm.gun import Gun


class TestGun(unittest.TestCase):

    def setUp(self):
        self.pistol = Gun("Pistol", "Glock", 10, "9mm")

    def test_given10_9mmBullets_whenLoaded_thenNumberOfBulletsIs10(self):
        bullets = []
        for count in range(10):
            bullets.append(Bullet("9mm"))
        print(f"\n{bullets}")

        self.pistol.load_magazine(bullets)

        self.assertEqual(10, self.pistol.number_of_bullets())

    def test_given10_10mmBullets_whenLoaded_thenNumberOfBulletsIs0(self):
        bullets = []
        for count in range(10):
            bullets.append(Bullet("10mm"))

        self.pistol.load_magazine(bullets)

        self.assertEqual(0, self.pistol.number_of_bullets())

    def test_given0Bullets_whenLoaded_thenNumberOfBulletsIs0(self):
        bullets = []
        self.pistol.load_magazine(bullets)

        self.assertEqual(0, self.pistol.number_of_bullets())

    def test_given11Bullets_whenLoaded_thenNumberOfBulletsIs10(self):
        bullets = []
        for count in range(11):
            bullets.append(Bullet("9mm"))

        self.pistol.load_magazine(bullets)

        self.assertEqual(10, self.pistol.number_of_bullets())

    def test_given5Bullets_whenFired_thenNumberOfBulletsIs4(self):
        bullets = []
        for count in range(5):
            bullets.append(Bullet("9mm"))

        self.pistol.load_magazine(bullets)
        self.pistol.fire()

        self.assertEqual(4, self.pistol.number_of_bullets())

    def test_given0Bullets_whenFired_thenMagazineIsEmpty(self):
        bullets = []
        for count in range(5):
            bullets.append(Bullet("9mm"))

        self.pistol.load_magazine(bullets)

        self.assertEqual("No bullet in the magazine", self.pistol.fire())
