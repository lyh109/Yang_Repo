import gfw

class Cookie:
    def __init__(self):
        self.cookie = gfw.Sprite('./res/Brave_Cookie.png')
        self.cookie.is_clip_image = True
        self.cookie.padding_size = 2
        self.cookie.cell_image_width = 270
        self.cookie.cell_image_height = 270
        self.cookie.cell_index_x = 1
        self.cookie.cell_index_y = 4
        self.cookie.scale_x = 1.0
        self.cookie.scale_y = 1.0
        gfw.renderer.add(self.cookie)

        self.elapsed_time = 0.0

    def update(self):
        self.cookie.x = 100.0
        self.cookie.y = 200.0

        self.elapsed_time += gfw.delta_time

        if self.elapsed_time >= 0.07:
            self.cookie.cell_index_x = int(self.cookie.cell_index_x + 1) % 4
            self.elapsed_time = 0.0