from firearm.magazine import Magazine


class Gun:
    def __init__(self, category: str, model: str, magazine_capacity: int, caliber: str):
        self.__category = category
        self.__model = model
        self.__magazine = Magazine(magazine_capacity)
        self.__caliber = caliber

    def load_magazine(self, *bullets):
        for bullet in bullets:
            if bullet.get_caliber() == self.__caliber:
                self.__magazine.load_bullet(bullet)

    def fire(self):
        bullet = self.__magazine.unload_bullet()
        if bullet:
            return f"Firing {self.__caliber} caliber bullet from {self.__model} {self.__category}"
        else:
            return "No bullet in the magazine"

    def number_of_bullets(self) -> int:
        return self.__magazine.number_of_bullets()
