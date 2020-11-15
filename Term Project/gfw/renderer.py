from gfw.sprite import Sprite

class Renderer:
    def __init__(self):
        self.sprites = []

    def draw(self):
        for i in self.sprites:
            if i.is_clip_image:
                i.image.clip_draw(i.padding_size + (i.cell_image_width + i.padding_size) * i.cell_index_x, 
                i.padding_size + (i.cell_image_height + i.padding_size) * i.cell_index_y, 
                i.cell_image_width, 
                i.cell_image_height, 
                i.x, 
                i.y)
            else:
                i.image.draw(i.x, i.y)

    def add(self, sprite):
        self.sprites.append(sprite)