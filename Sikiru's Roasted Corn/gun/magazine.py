class Magazine:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.bullets = []

    def load_bullet(self, bullet):
        if len(self.bullets) < self.capacity:
            self.bullets.append(bullet)

    def unload_bullet(self):
        self.bullets.pop()

    def fire_bullet(self):
        if self.bullets:
            return self.unload_bullet()
        else:
            return "Magazine is empty"
