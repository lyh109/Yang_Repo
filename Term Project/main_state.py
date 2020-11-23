import gfw
from cookie import Cookie
from background import Background

class MainState:
    def init(self):
        self.background1 = Background('./res/bk11-1.png', 2, 0.1)
        self.background2 = Background('./res/bk11-2.png', 3, 0.2)
        self.background3 = Background('./res/bk11-3.png', 2, 0.4)
        self.background4 = Background('./res/bk11-4.png', 2, 0.6)

        self.cookie = Cookie()

    def update(self):
        self.cookie.update()
        self.background1.update()
        self.background2.update()
        self.background3.update()
        self.background4.update()

        if gfw.eh.get_mouse_button(gfw.eh.LBUTTON):
            print(gfw.eh.mouse_pos[0])

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()