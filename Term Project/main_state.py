from gfw import sprite
from pico2d import *
import json

import gfw
from cookie import Cookie
from background import Background
from item import Item

class MainState:
    def init(self):
        # self.bgm = load_music('./res/sound/bgm_gameplay.ogg')
        # self.bgm.repeat_play()
        
        self.background1 = Background('./res/bk/bk11-1.png', 2, 0.1, 2)
        self.background2 = Background('./res/bk/bk11-2.png', 3, 0.2, 2)
        self.background3 = Background('./res/bk/bk11-3.png', 2, 0.4, 2)
        self.background4 = Background('./res/bk/bk11-4.png', 2, 0.6, 2)
        self.tile = Background('./res/tile/tile11.png', 12, 3.0, 1)
        
        self.cookie = Cookie()

        objects = None
        with open('./res/data/objects.json') as f:
            objects = json.load(f)

        for o in objects:
            item = Item(o)

    def update(self):
        self.cookie.update()
        self.background1.update()
        self.background2.update()
        self.background3.update()
        self.background4.update()
        self.tile.update()

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()