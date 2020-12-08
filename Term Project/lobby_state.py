from gfw.events_handler import LBUTTON
import gfw
from main_state import MainState
from pico2d import *

NONE = -1
BRAVE_COOKIE = 0
ZOMBIE_COOKIE = 1

class LobbyState:
    def init(self):
        self.__init()
    
    def update(self):
        mouse_x, mouse_y = gfw.eh.mouse_pos[0],  gfw.eh.mouse_pos[1]
        selected_cookie = NONE

        brave_cookie_half_w = self.brave_cookie.image.w * 0.5
        brave_cookie_half_h = self.brave_cookie.image.h * 0.5
        if self.brave_cookie.x - brave_cookie_half_w <= mouse_x and mouse_x <= self.brave_cookie.x + brave_cookie_half_w and self.brave_cookie.y - brave_cookie_half_h <= mouse_y and mouse_y < self.brave_cookie.y + brave_cookie_half_h:
            self.brave_cookie.scale_x = 1.2
            self.brave_cookie.scale_y = 1.2
            selected_cookie = BRAVE_COOKIE
        else:
            self.brave_cookie.scale_x = 1.0
            self.brave_cookie.scale_y = 1.0

        zombie_cookie_half_w = self.zombie_cookie.image.w * 0.5
        zombie_cookie_half_h = self.zombie_cookie.image.h * 0.5
        if self.zombie_cookie.x - zombie_cookie_half_w <= mouse_x and mouse_x <= self.zombie_cookie.x + zombie_cookie_half_w and self.zombie_cookie.y - zombie_cookie_half_h <= mouse_y and mouse_y < self.zombie_cookie.y + zombie_cookie_half_h:
            self.zombie_cookie.scale_x = 1.2
            self.zombie_cookie.scale_y = 1.2
            selected_cookie = ZOMBIE_COOKIE
        else:
            self.zombie_cookie.scale_x = 1.0
            self.zombie_cookie.scale_y = 1.0

        if selected_cookie != NONE:
            if gfw.eh.get_mouse_button_down(LBUTTON):
                self.select_sound.play()
                self.start_sound.play()
                self.black_screen.active = True

        if self.black_screen.active:
            self.black_screen.alpha = min(1.0, self.black_screen.alpha + gfw.delta_time * 2.0)
            if self.black_screen.alpha >= 1.0:
                gfw.push_state(MainState(selected_cookie))

    def pause(self):
        pass

    def resume(self):
        self.__init()

    def exit(self):
        pass

    def __init(self):
        back = gfw.Sprite('./res/lobby_back.png')
        back.x = gfw.SCREEN_WIDTH * 0.5
        back.y = gfw.SCREEN_HEIGHT * 0.5
        gfw.renderer.add(back)

        self.brave_cookie = gfw.Sprite('./res/GingerBrave.png')
        self.brave_cookie.x = gfw.SCREEN_WIDTH * 0.5 - 200.0
        self.brave_cookie.y = gfw.SCREEN_HEIGHT * 0.5 - 100.0
        gfw.renderer.add(self.brave_cookie)

        self.zombie_cookie = gfw.Sprite('./res/Zombie Cookie.png')
        self.zombie_cookie.x = gfw.SCREEN_WIDTH * 0.5 + 200.0
        self.zombie_cookie.y = gfw.SCREEN_HEIGHT * 0.5 - 100.0
        gfw.renderer.add(self.zombie_cookie)

        self.black_screen = gfw.Sprite('./res/bk/bb.png')
        self.black_screen.x = gfw.SCREEN_WIDTH * 0.5
        self.black_screen.y = gfw.SCREEN_HEIGHT * 0.5
        self.black_screen.alpha = 0.0
        self.black_screen.active = False
        gfw.renderer.add(self.black_screen)

        self.bgm = load_music('./res/sound/bgm_lobby.mp3')
        self.bgm.repeat_play()

        self.select_sound = load_wav('./res/sound/button_on.wav')
        self.start_sound = load_wav('./res/sound/start.wav')


if __name__ == '__main__':
    gfw.init(LobbyState())
    gfw.run()