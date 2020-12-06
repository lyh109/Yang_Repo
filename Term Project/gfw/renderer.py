from gfw.sprite import Sprite

class Renderer:
    def __init__(self):
        self.sprites = []
        self.fonts = []

    def draw(self):
        for i in self.sprites:
            if i.active == False:
                continue

            i.image.opacify(i.alpha)

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

        for i in self.fonts:
            i.ttf.draw(i.x, i.y, i.text, (i.color_r, i.color_g, i.color_b))

    def add(self, sprite):
        self.sprites.append(sprite)

    def add_font(self, font):
        self.fonts.append(font)