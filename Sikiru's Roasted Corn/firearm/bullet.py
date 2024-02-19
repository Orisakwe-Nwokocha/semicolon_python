class Bullet:
    def __init__(self, caliber: str):
        self.__caliber = caliber

    def get_caliber(self) -> str:
        return self.__caliber

    def __repr__(self):
        return f"{self.__caliber} bullet"
