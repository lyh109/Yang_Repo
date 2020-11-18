import gfw
from cookie import Cookie
from background import Background

class MainState:
    def init(self):
        self.background = Background('./res/bk1-1.png', 2, 0.15)
        self.background = Background('./res/bk1-2.png', 2, 0.3)
       
        self.cookie = Cookie()

    def update(self):
        self.cookie.update()
        self.background.update()

        if gfw.eh.get_mouse_button(gfw.eh.LBUTTON):
            print(gfw.eh.mouse_pos[0])

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()