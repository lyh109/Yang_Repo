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

    def update(self):
        self.speedY -= ACC
        self.cookie.y += self.speedY

        if self.cookie.y <= MIN_Y:
            self.cookie.y = MIN_Y
            self.speedY = 0.0
            
            if self.state >= JUMP:
                self.state = RUN

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