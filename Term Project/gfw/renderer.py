from gfw.sprite import Sprite

class Renderer:
    def __init__(self):
        self.sprites = []

    def draw(self):
        for i in self.sprites:
            if i.active == False:
                continue

            if i.is_clip_image:
                i.image.clip_draw(i.padding_size + (i.cell_image_width + i.padding_size) * i.cell_index_x, 
                i.padding_size + (i.cell_image_height + i.padding_size) * i.cell_index_y, 
                i.cell_image_width, 
                i.cell_image_height, 
                i.x, 
                i.y,
                i.cell_image_width * i.scale_x,
                i.cell_image_height * i.scale_y)
            else:
                x = i.x + i.image.w * i.scale_x * (0.5 - i.origin_x)
                y = i.y + i.image.h * i.scale_y * (0.5 - i.origin_y)
                i.image.draw(x, y, i.image.w * i.scale_x, i.image.h * i.scale_y)

    def add(self, sprite):
        self.sprites.append(sprite)