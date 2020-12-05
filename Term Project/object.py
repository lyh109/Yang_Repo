from pico2d import *
import gfw

class Object:
    def __init__(self, data, offset_x):
        self.spr = None

    def update(self):
        self.spr.x -= 200.0 * gfw.delta_time
        
        self.col_box_x = self.spr.x
        self.col_box_y = self.spr.y

    def init_col_box(self):
        self.col_box_x = self.spr.x
        self.col_box_y = self.spr.y

        if self.spr.is_clip_image:
            self.col_box_w = self.spr.cell_image_width
            self.col_box_h = self.spr.cell_image_height
        else:
            self.col_box_w = self.spr.image.w
            self.col_box_h = self.spr.image.h

    def get_col_box(self):
        left = self.col_box_x - self.col_box_w * 0.5
        right = self.col_box_x + self.col_box_w * 0.5
        bottom = self.col_box_y - self.col_box_h * 0.5
        top = self.col_box_y + self.col_box_h * 0.5
        
        return left, right, bottom, top
        

class Jelly(Object):
    def __init__(self, data, offset_x):
        super().__init__(data, offset_x)

        self.ate_sound = load_wav('./res/sound/jelly.ogg')
        self.frame_count = 0
        self.kind = int(data['name'][1])

        if data['name'] == 'j0' or data['name'] == 'j1':
            self.spr = gfw.Sprite('./res/basic_jellies.png')
            self.frame_count = 3
            self.spr.cell_image_width = 38
            self.spr.cell_index_x = self.kind * self.frame_count
        else:
            self.spr = gfw.Sprite('./res/bear_jellies.png')
            if self.kind % 2 == 0:
                self.frame_count = 1
            else:
                self.frame_count = 2

            if self.kind == 2:
                self.spr.cell_index_x = 0
            elif self.kind == 3:
                self.spr.cell_index_x = 1
            elif self.kind == 4:
                self.spr.cell_index_x = 3
            elif self.kind == 5:
                self.spr.cell_index_x = 4
            elif self.kind == 6:
                self.spr.cell_index_x = 6
            elif self.kind == 7:
                self.spr.cell_index_x = 7
            elif self.kind == 8:
                self.spr.cell_index_x = 9
            elif self.kind == 9:
                self.spr.cell_index_x = 10

            self.spr.cell_image_width = 55

        self.spr.cell_image_height = 51       
        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]
        self.spr.is_clip_image = True
        self.spr.padding_size = 2
        self.spr.cell_index_y = 0
        self.score = 0.0
        gfw.renderer.add(self.spr)

        self.init_col_box()

class Tile(Object):
    def __init__(self, data, offset_x):
        self.spr = gfw.Sprite('./res/stage/11/t1.png')
        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]
        gfw.renderer.add(self.spr)

        self.init_col_box()

        