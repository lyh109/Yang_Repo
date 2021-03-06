from pico2d import *

images = {}

class Sprite:
    def __init__(self, image_path):
        self.x = 0.0
        self.y = 0.0
        self.scale_x = 1.0
        self.scale_y = 1.0
        self.origin_x = 0.5
        self.origin_y = 0.5
        self.active = True
        self.alpha = 1.0
        self.image = None
        
        self.is_clip_image = False
        self.cell_image_width = 0
        self.cell_image_height = 0
        self.cell_index_x = 0
        self.cell_index_y = 0
        self.padding_size = 0
        
        if not image_path in images:
            images[image_path] = load_image(image_path)

        self.image = images[image_path]