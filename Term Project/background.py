import gfw

class Background:
    def __init__(self):
        self.background = gfw.Sprite('./res/bk1.png')
        self.background.scale_x = 2.0
        self.background.scale_y = 2.0
        self.background.origin_x = 0.0
        self.background.origin_y = 0.0
        gfw.renderer.add(self.background)