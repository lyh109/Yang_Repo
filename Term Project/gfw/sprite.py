from pico2d import *

class Sprite:
    def __init__(self, image_path = None):
        self.x = 0.0
        self.y = 0.0
        self.image = None
        self.is_clip_image = False
        self.cell_image_width = 0
        self.cell_image_height = 0
        self.cell_index_x = 0
        self.cell_index_y = 0
        self.padding_size = 0
        
        if not image_path is None:
            self.image = load_image(image_path)