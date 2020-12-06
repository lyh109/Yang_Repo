from pico2d import *
import gfw
import random

class Object:
    def __init__(self, data, offset_x):
        self.spr = None

    def update(self):
        self.spr.x -= 450.0 * gfw.delta_time
        
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

        self.ate_sound = load_wav('./res/sound/jelly.wav')
        self.frame_count = 0
        self.kind = int(data['name'][1])

        if data['name'] == 'j0' or data['name'] == 'j1':
            self.spr = gfw.Sprite('./res/basic_jellies.png')
            self.frame_count = 3
            self.spr.cell_image_width = 38
            self.spr.cell_index_x = self.kind * self.frame_count
            self.score = 10
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
            self.score = 20

        self.spr.cell_image_height = 51       
        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]
        self.spr.is_clip_image = True
        self.spr.padding_size = 2
        self.spr.cell_index_y = 0

        gfw.renderer.add(self.spr)

        self.init_col_box()

class Tile(Object):
    def __init__(self, data, offset_x):
        super().__init__(data, offset_x)

        self.spr = gfw.Sprite('./res/stage/6/t1.png')
        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]
        gfw.renderer.add(self.spr)

        self.init_col_box()

class Obstacle(Object):
    def __init__(self, data, offset_x):
        super().__init__(data, offset_x)

        self.kind = data['name'][1]
        self.spr = gfw.Sprite('./res/stage/6/o' + self.kind + '.png')
        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]

        if int(self.kind) > 4:
            self.spr.is_clip_image = True
            self.spr.padding_size = 0
            
            self.spr.cell_index_x = 0
            self.spr.cell_index_y = 0
            if int(self.kind) == 5:
                self.spr.cell_image_width = 69
                self.spr.cell_image_height = 131
            elif int(self.kind) == 6:
                self.spr.cell_image_width = 118
                self.spr.cell_image_height = 249

        gfw.renderer.add(self.spr)

        self.init_col_box()
        self.elapsed_time = 0.0

    def update(self):
        super().update()
        
        self.elapsed_time += gfw.delta_time
        if self.spr.is_clip_image and self.spr.x < 600 and self.spr.cell_index_x < int(self.kind) - 2:
            if self.elapsed_time >= 0.1:
                self.spr.cell_index_x += 1
                self.elapsed_time = 0.0

class Dessert(Object):
    def __init__(self, data, offset_x):
        super().__init__(data, offset_x)

        self.ate_sound = load_wav('./res/sound/dessert.wav')
        self.spr = gfw.Sprite('./res/desserts.png')
        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]
        self.spr.cell_image_width = 66
        self.spr.cell_image_height = 66
        self.spr.is_clip_image = True
        self.spr.padding_size = 2

        self.kind = random.randrange(0, 30)
        self.spr.cell_index_x = self.kind
        self.spr.cell_index_y = 0

        gfw.renderer.add(self.spr)

        self.score = 30
        self.init_col_box()
        
class Potion(Object):
    def __init__(self, data, offset_x):
        super().__init__(data, offset_x)
        
        self.kind = data['name'][1]
        self.ate_sound = load_wav('./res/sound/hpup_' + self.kind + '.wav')
        self.spr = gfw.Sprite('./res/potion_' + self.kind + '.png')

        self.spr.x = data["x"] + offset_x
        self.spr.y = data["y"]

        if self.kind == '1':
            self.spr.is_clip_image = True
            self.spr.cell_image_width = 144
            self.spr.cell_image_height = 144
            self.spr.padding_size = 2
            self.spr.cell_index_x = 0
            self.spr.cell_index_y = 0

        gfw.renderer.add(self.spr)

        self.elapsed_time = 0.0
        self.init_col_box()

    def update(self):
        super().update()
        self.elapsed_time += gfw.delta_time

        if self.spr.is_clip_image:
            if self.elapsed_time >= 0.1:
                self.spr.cell_index_x = int(self.spr.cell_index_x + 1) % 4
                self.elapsed_time = 0.0
