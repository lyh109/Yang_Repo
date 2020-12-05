from importlib.util import spec_from_loader
from pico2d import *
import gfw

ACC = 0.25
RUN = 0
JUMP = 1
DOUBLE_JUMP = 2
SLIDE = -1
MIN_Y = 250.0

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
        self.cookie.x = 100.0
        self.cookie.y = MIN_Y      
        gfw.renderer.add(self.cookie)

        self.acc = 0.0
        self.elapsed_time = 0.0
        self.speedY = 0.0
        self.state = RUN

        self.jump_sound = load_wav('./res/sound/jump.ogg')
        self.slide_sound = load_wav('./res/sound/slide.ogg')

        self.col_box_x = self.cookie.x
        self.col_box_y = self.cookie.y

        self.col_box_w = 100
        self.col_box_h = 130        

    def update(self, tiles):
        self.speedY -= ACC
        to_y = self.cookie.y + self.speedY

        col_box_w, col_box_h, col_box_x, col_box_y = 0.0, 0.0, 0.0, 0.0
        if self.state == RUN:
            col_box_w = 100
            col_box_h = 130
            col_box_x = self.cookie.x
            col_box_y = to_y - 65.0
        elif self.state == SLIDE:
            col_box_w = 160
            col_box_h = 70
            col_box_x = self.cookie.x
            col_box_y = to_y - 100.0
        elif self.state == JUMP:
            col_box_w = 100
            col_box_h = 120
            col_box_x = self.cookie.x
            col_box_y = to_y - 80.0
        elif self.state == DOUBLE_JUMP:
            col_box_w = 100
            col_box_h = 130
            col_box_x = self.cookie.x
            col_box_y = to_y - 65.0 
            
        if to_y <= MIN_Y:
            to_y = MIN_Y
            self.speedY = 0.0

            if self.state >= JUMP:
                self.state = RUN
        elif self.speedY < 0.0:
            cookie_left = col_box_x - col_box_w * 0.5
            cookie_right = col_box_x + col_box_w * 0.5
            cookie_bottom = col_box_y - col_box_h * 0.5
            cookie_top = col_box_y + col_box_h * 0.5

            for i in tiles:
                left, right, bottom, top = i.get_col_box()
                if cookie_left <= right and cookie_right >= left and cookie_bottom <= top and cookie_top >= bottom:
                    self.speedY = 0.0

                    if self.state >= JUMP:
                        self.state = RUN

                    to_y = top + 130
                    break
        
        self.cookie.y = to_y

        if gfw.eh.get_key_down(gfw.SDLK_SPACE):
            if self.state < DOUBLE_JUMP:
                self.speedY = 8.0
                self.state = JUMP if self.state < JUMP else DOUBLE_JUMP
                self.cookie.cell_index_x = 1
                self.jump_sound.play()
        elif gfw.eh.get_key(gfw.SDLK_DOWN):
            if self.state == RUN:
                self.state = SLIDE
                self.slide_sound.play()
        elif gfw.eh.get_key_up(gfw.SDLK_DOWN):
            if self.state == SLIDE:
                self.state = RUN

        if self.state == RUN:
            self.col_box_w = 100
            self.col_box_h = 130
            self.col_box_x = self.cookie.x
            self.col_box_y = self.cookie.y - 65.0
        elif self.state == SLIDE:
            self.col_box_w = 160
            self.col_box_h = 70
            self.col_box_x = self.cookie.x
            self.col_box_y = self.cookie.y - 100.0
        elif self.state == JUMP:
            self.col_box_w = 100
            self.col_box_h = 120
            self.col_box_x = self.cookie.x
            self.col_box_y = self.cookie.y - 80.0
        elif self.state == DOUBLE_JUMP:
            self.col_box_w = 100
            self.col_box_h = 130
            self.col_box_x = self.cookie.x
            self.col_box_y = self.cookie.y - 65.0

        # Update animation
        self.elapsed_time += gfw.delta_time
        if self.elapsed_time >= 0.07:
            if self.state == RUN:
                self.cookie.cell_index_x = int(self.cookie.cell_index_x + 1) % 4
                self.cookie.cell_index_y = 4
            elif self.state == JUMP:
                self.cookie.cell_index_x = 7
                self.cookie.cell_index_y = 5
            elif self.state == DOUBLE_JUMP:
                self.cookie.cell_index_x = int(self.cookie.cell_index_x + 1) % 6
                self.cookie.cell_index_y = 5
            elif self.state == SLIDE:
                self.cookie.cell_index_x = 9
                self.cookie.cell_index_y = 5
            self.elapsed_time = 0.0

    def get_col_box(self):
        left = self.col_box_x - self.col_box_w * 0.5
        right = self.col_box_x + self.col_box_w * 0.5
        bottom = self.col_box_y - self.col_box_h * 0.5
        top = self.col_box_y + self.col_box_h * 0.5

        return left, right, bottom, top

        