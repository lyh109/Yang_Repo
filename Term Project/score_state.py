import gfw
from gfw import SCREEN_HEIGHT, SCREEN_WIDTH, sprite
from gfw.events_handler import LBUTTON
from pico2d import *

class ScoreState:
    def __init__(self, score):
        self.score = score

    def init(self):
        self.__init()
        
    
    def update(self):
        self.font.text = 'SCORE: ' + str(int(self.score))
        mouse_x, mouse_y = gfw.eh.mouse_pos[0],  gfw.eh.mouse_pos[1]
        r_button_half_w = self.ok_button.image.w * 0.5
        r_button_half_h = self.ok_button.image.h * 0.5
        e_button_half_w = self.ok_button.image.w * 0.5
        e_button_half_h = self.ok_button.image.h * 0.5

        if self.ok_button.x - r_button_half_w <= mouse_x and mouse_x <= self.ok_button.x + r_button_half_w and self.ok_button.y - r_button_half_h <= mouse_y and mouse_y < self.ok_button.y + r_button_half_h:
            self.ok_button.scale_x = 1.2
            self.ok_button.scale_y = 1.2
            if gfw.eh.get_mouse_button_down(LBUTTON):
                self.select_button.play()
                self.black_screen.active = True
        else:
            self.ok_button.scale_x = 1.0
            self.ok_button.scale_y = 1.0

        if self.black_screen.active:
            self.black_screen.alpha = min(1.0, self.black_screen.alpha + gfw.delta_time * 2.0)
            if self.black_screen.alpha >= 1.0:
                gfw.pop_state()
                gfw.pop_state()

    def pause(self):
        pass

    def resume(self):
        self.__init()

    def exit(self):
        pass

    def __init(self):
        back = gfw.Sprite('./res/bk/bb.png')
        back.x = gfw.SCREEN_WIDTH * 0.5
        back.y = gfw.SCREEN_HEIGHT * 0.5
        gfw.renderer.add(back)

        self.font = gfw.Text('./res/font.ttf', 48)
        self.font.x = SCREEN_WIDTH - 680.0
        self.font.y = SCREEN_HEIGHT * 0.5
        self.font.color_r = 255
        self.font.color_g = 255
        self.font.color_b = 255
        self.font.text = 'SCORE: 0'
        gfw.renderer.add_font(self.font)

        self.black_screen = gfw.Sprite('./res/bk/bb.png')
        self.black_screen.x = gfw.SCREEN_WIDTH * 0.5
        self.black_screen.y = gfw.SCREEN_HEIGHT * 0.5
        self.black_screen.alpha = 0.0
        self.black_screen.active = False
        gfw.renderer.add(self.black_screen)

        self.ok_button = gfw.Sprite('./res/ok_button.png')
        self.ok_button.x = SCREEN_WIDTH * 0.5
        self.ok_button.y = SCREEN_HEIGHT * 0.3
        gfw.renderer.add(self.ok_button)

        self.bgm_score = load_wav('./res/sound/score.wav')
        self.select_button = load_wav('./res/sound/button_off.wav')

        self.bgm_score.play()

if __name__ == '__main__':
    gfw.init(ScoreState(0))
    gfw.run()