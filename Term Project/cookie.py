from importlib.util import spec_from_loader

from pico2d import *

import gfw

ACC = 1.0
RUN = 0
JUMP = 1
DOUBLE_JUMP = 2
SLIDE = -1

class Cookie:
    def __init__(self, image_path, cell_image_w, cell_image_h, min_y, tile_y):
        self.min_y = min_y
        self.tile_y = tile_y

        self.cookie = gfw.Sprite(image_path)
        self.cookie.is_clip_image = True
        self.cookie.padding_size = 2
        self.cookie.cell_image_width = cell_image_w
        self.cookie.cell_image_height = cell_image_h
        self.cookie.cell_index_x = 1
        self.cookie.cell_index_y = 4
        self.cookie.scale_x = 1.0
        self.cookie.scale_y = 1.0
        self.cookie.x = 120.0
        self.cookie.y = self.min_y        

        gfw.renderer.add(self.cookie)

        self.acc = 0.0
        self.elapsed_time = 0.0
        self.speedY = 0.0
        self.state = RUN

        self.jump_sound = load_wav('./res/sound/jump.wav')
        self.slide_sound = load_wav('./res/sound/slide.wav')

        self.col_box_x = self.cookie.x
        self.col_box_y = self.cookie.y
        self.col_box_w = 0.0
        self.col_box_h = 0.0

        self.run_col_box_w = 0.0
        self.run_col_box_h = 0.0
        self.run_col_offset_y = 0.0

        self.slide_col_box_w = 0.0
        self.slide_col_box_h = 0.0
        self.slide_col_offset_y = 0.0

        self.jump_col_box_w = 0.0
        self.jump_col_box_h = 0.0
        self.jump_col_offset_y = 0.0

        self.djump_col_box_w = 0.0
        self.djump_col_box_h = 0.0
        self.djump_col_offset_y = 0.0

        self.hp = 100.0

    def update(self, tiles):
        if self.hp > 0.0:
            self.DoAction(tiles)

        # Update animation
        self.elapsed_time += gfw.delta_time
        if self.elapsed_time >= 0.07:
            if self.hp > 0.0:
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
            else:
                self.cookie.cell_index_x = max(5, min(9, self.cookie.cell_index_x + 1))
                self.cookie.cell_index_y = 1
                
            self.elapsed_time = 0.0

    def get_col_box(self):
        left = self.col_box_x - self.col_box_w * 0.5
        right = self.col_box_x + self.col_box_w * 0.5
        bottom = self.col_box_y - self.col_box_h * 0.5
        top = self.col_box_y + self.col_box_h * 0.5

        return left, right, bottom, top

    def hit(self, dhp):
        self.hp -= dhp

        if self.hp > 0.0:   
            self.cookie.alpha = 0.5
            return True

        return False

    def DoAction(self, tiles):
        self.speedY -= ACC
        to_y = self.cookie.y + self.speedY

        col_box_w, col_box_h, col_box_x, col_box_y = 0.0, 0.0, 0.0, 0.0
        if self.state == RUN:
            col_box_w = self.run_col_box_w
            col_box_h = self.run_col_box_h
            col_box_x = self.cookie.x
            col_box_y = to_y - self.run_col_offset_y
        elif self.state == SLIDE:
            col_box_w = self.slide_col_box_w
            col_box_h = self.slide_col_box_h
            col_box_x = self.cookie.x
            col_box_y = to_y - self.slide_col_offset_y
        elif self.state == JUMP:
            col_box_w = self.jump_col_box_w
            col_box_h = self.jump_col_box_h
            col_box_x = self.cookie.x
            col_box_y = to_y - self.jump_col_offset_y
        elif self.state == DOUBLE_JUMP:
            col_box_w = self.djump_col_box_w
            col_box_h = self.djump_col_box_h
            col_box_x = self.cookie.x
            col_box_y = to_y - self.djump_col_offset_y 
            
        if to_y <= self.min_y:
            to_y = self.min_y
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

                    to_y = top + self.tile_y
                    break
        
        self.cookie.y = to_y

        if gfw.eh.get_key_down(gfw.SDLK_SPACE):
            if self.state < DOUBLE_JUMP:
                self.speedY = 21.0
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
            self.col_box_w = self.run_col_box_w
            self.col_box_h = self.run_col_box_h
            self.col_box_x = self.cookie.x
            self.col_box_y = to_y - self.run_col_offset_y
        elif self.state == SLIDE:
            self.col_box_w = self.slide_col_box_w
            self.col_box_h = self.slide_col_box_h
            self.col_box_x = self.cookie.x
            self.col_box_y = to_y - self.slide_col_offset_y
        elif self.state == JUMP:
            self.col_box_w = self.jump_col_box_w
            self.col_box_h = self.jump_col_box_h
            self.col_box_x = self.cookie.x
            self.col_box_y = to_y - self.jump_col_offset_y
        elif self.state == DOUBLE_JUMP:
            self.col_box_w = self.djump_col_box_w
            self.col_box_h = self.djump_col_box_h
            self.col_box_x = self.cookie.x
            self.col_box_y = to_y - self.djump_col_offset_y

        self.cookie.alpha = min(1.0, self.cookie.alpha + 0.5 * gfw.delta_time)
    
class BraveCookie(Cookie):
    def __init__(self):
        super().__init__('./res/Brave_Cookie.png', 270, 270, 250.0, 130.0)

        self.run_col_box_w = 100.0
        self.run_col_box_h = 130.0
        self.run_col_offset_y = 65.0

        self.slide_col_box_w = 160.0
        self.slide_col_box_h = 70.0
        self.slide_col_offset_y = 100.0

        self.jump_col_box_w = 100.0
        self.jump_col_box_h = 120.0
        self.jump_col_offset_y = 80.0

        self.djump_col_box_w = 100.0
        self.djump_col_box_h = 130.0
        self.djump_col_offset_y = 65.0
        
class ZombieCookie(Cookie):
    def __init__(self):
        super().__init__('./res/Zombie_Cookie.png', 320, 320, 275.0, 150.0)

        self.life = 2

        self.run_col_box_w = 100.0
        self.run_col_box_h = 130.0
        self.run_col_offset_y = 90.0

        self.slide_col_box_w = 160.0
        self.slide_col_box_h = 70.0
        self.slide_col_offset_y = 120.0

        self.jump_col_box_w = 100.0
        self.jump_col_box_h = 110.0
        self.jump_col_offset_y = 95.0

        self.djump_col_box_w = 100.0
        self.djump_col_box_h = 130.0
        self.djump_col_offset_y = 75.0

