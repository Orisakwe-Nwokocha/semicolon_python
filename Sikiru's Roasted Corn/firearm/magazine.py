class Magazine:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__bullets = []

    def load_bullet(self, bullet):
        if len(self.__bullets) < self.__capacity:
            self.__bullets.append(bullet)

    def unload_bullet(self):
        self.__bullets.pop()

    def fire_bullet(self):
        if self.__bullets:
            return self.unload_bullet()
        else:
            return "Magazine is empty"

    def number_of_bullets(self) -> int:
        return len(self.__bullets)
