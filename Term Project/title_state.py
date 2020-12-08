import gfw
from gfw import SCREEN_HEIGHT, SCREEN_WIDTH, sprite
from gfw.events_handler import LBUTTON
from pico2d import *
from lobby_state import LobbyState

class TitleState:
    def init(self):
        self.__init()
        
    
    def update(self):
        self.white_screen.alpha = min(1.0, self.white_screen.alpha + gfw.delta_time)
        if self.white_screen.active and self.white_screen.alpha >= 1.0:
            self.loading_done.play()
            self.white_screen.active = False
            self.back_kpu.active = False

        if gfw.eh.get_key_down(SDLK_SPACE):
            self.black_screen.active = True
            self.pressed_button.play()
        
        if self.black_screen.active:
            self.black_screen.alpha = min(1.0, self.white_screen.alpha + gfw.delta_time)
            if self.black_screen.alpha >= 1.0:
                gfw.push_state(LobbyState())

    def pause(self):
        pass

    def resume(self):
        self.__init()

    def exit(self):
        pass

    def __init(self):
        self.back = gfw.Sprite('./res/title.png')
        self.back.x = gfw.SCREEN_WIDTH * 0.5
        self.back.y = gfw.SCREEN_HEIGHT * 0.5
        gfw.renderer.add(self.back)

        self.back_kpu = gfw.Sprite('./res/title_kpu.png')
        self.back_kpu.x = gfw.SCREEN_WIDTH * 0.5
        self.back_kpu.y = gfw.SCREEN_HEIGHT * 0.5
        gfw.renderer.add(self.back_kpu)

        self.white_screen = gfw.Sprite('./res/bk/bw.png')
        self.white_screen.x = gfw.SCREEN_WIDTH * 0.5
        self.white_screen.y = gfw.SCREEN_HEIGHT * 0.5
        self.white_screen.alpha = 0.0
        gfw.renderer.add(self.white_screen)

        self.black_screen = gfw.Sprite('./res/bk/bb.png')
        self.black_screen.x = gfw.SCREEN_WIDTH * 0.5
        self.black_screen.y = gfw.SCREEN_HEIGHT * 0.5
        self.black_screen.alpha = 0.0
        self.black_screen.active = False
        gfw.renderer.add(self.black_screen)


        self.loading = load_wav('./res/sound/loading.wav')
        self.pressed_button = load_wav('./res/sound/button_on.wav')
        self.loading_done = load_wav('./res/sound/title.wav')

        self.loading.play()

if __name__ == '__main__':
    gfw.init(TitleState())
    gfw.run()