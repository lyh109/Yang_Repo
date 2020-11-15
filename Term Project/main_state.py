import gfw
from cookie import Cookie
from background import Background

class MainState:
    def init(self):
        self.background = Background('./res/bk2.png')
        self.background.repeat_count = 2
        self.background.speed = 0.5

        self.cookie = Cookie()

    def update(self):
        self.cookie.update()
        self.background.update()

        if gfw.eh.get_mouse_button(gfw.eh.LBUTTON):
            print(gfw.eh.mouse_pos[0])

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()