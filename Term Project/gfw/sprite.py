from pico2d import *

class Sprite:
    def __init__(self, image_path = None):
        self.x = 0.0
        self.y = 0.0
        self.image = None

        if not image_path is None:
            self.image = load_image(image_path)