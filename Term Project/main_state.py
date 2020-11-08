import gfw

class MainState:
    def init(self):
        self.cookie = gfw.Sprite('./res/Brave_Cookie.png')
        gfw.renderer.add(self.cookie)

    def update(self):
        self.cookie.x += 100.0 * gfw.delta_time

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()