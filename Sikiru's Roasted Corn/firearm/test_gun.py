import unittest

from firearm.bullet import Bullet
from firearm.gun import Gun


class TestGun(unittest.TestCase):

    def setUp(self):
        self.pistol = Gun("Pistol", "Glock", 10, "9mm")

    def test_given10_9mmBullets_whenLoaded_thenNumberOfBulletsIs10(self):
        for count in range(10):
            self.pistol.load_magazine(Bullet("9mm"))

        self.assertEqual(10, self.pistol.number_of_bullets())

    def test_given10_10mmBullets_whenLoaded_thenNumberOfBulletsIs0(self):
        for count in range(10):
            self.pistol.load_magazine(Bullet("10mm"))

        self.assertEqual(0, self.pistol.number_of_bullets())

    def test_that_magazine_is_empty(self):
        self.assertEqual(0, self.pistol.number_of_bullets())

    def test_given11Bullets_whenLoaded_thenNumberOfBulletsIs10(self):
        for count in range(10):
            self.pistol.load_magazine(Bullet("9mm"))
        self.assertEqual(10, self.pistol.number_of_bullets())

        bullet = Bullet("9mm")
        print(bullet)
        self.assertEqual(10, self.pistol.number_of_bullets())

    def test_given5Bullets_whenFired_thenNumberOfBulletsIs4(self):
        for count in range(5):
            self.pistol.load_magazine(Bullet("9mm"))

        self.pistol.toggle()
        print(self.pistol.fire())

        self.assertEqual(4, self.pistol.number_of_bullets())

    def test_given0Bullets_whenFired_thenMagazineIsEmpty(self):
        self.pistol.toggle()
        self.assertEqual("No bullet in the magazine", self.pistol.fire())

    def test_safetyIsOn_turnItOff_safetyIsOff(self):
        self.assertTrue(self.pistol.is_on())

        self.pistol.toggle()
        self.assertFalse(self.pistol.is_on())

    def test_safetyIsOff_turnItOn_safetyIsOn(self):
        self.pistol.toggle()
        self.assertFalse(self.pistol.is_on())

        self.pistol.toggle()
        self.assertTrue(self.pistol.is_on())
