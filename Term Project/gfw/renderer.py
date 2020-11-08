from gfw.sprite import Sprite

class Renderer:
    def __init__(self):
        self.sprites = []

    def draw(self):
        for i in self.sprites:
            i.image.draw(i.x, i.y)

    def add(self, sprite):
        self.sprites.append(sprite)