from gun.magazine import Magazine


class Gun:
    def __init__(self, category: str, model: str, magazine_capacity: int, caliber: str):
        self.category = category
        self.model = model
        self.magazine = Magazine(magazine_capacity)
        self.caliber = caliber

    def load_magazine(self, bullets):
        for bullet in bullets:
            if bullet.caliber == self.caliber:
                self.magazine.load_bullet(bullet)

    def fire(self):
        bullet = self.magazine.fire_bullet()
        if bullet:
            return f"Firing {self.caliber} caliber bullet from {self.model} {self.category}"
        else:
            return f"No bullet in the magazine"
