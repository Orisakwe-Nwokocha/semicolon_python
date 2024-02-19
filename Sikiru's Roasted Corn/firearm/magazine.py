class Magazine:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__bullets = []

    def load_bullet(self, bullet):
        if len(self.__bullets) < self.__capacity:
            self.__bullets.append(bullet)

    def unload_bullet(self):
        if self.__bullets:
            return self.__bullets.pop()

    def number_of_bullets(self) -> int:
        return len(self.__bullets)
