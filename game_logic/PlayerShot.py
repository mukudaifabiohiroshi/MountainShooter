from game_logic.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self,):
        self.rect.x += self.rect.width / 2