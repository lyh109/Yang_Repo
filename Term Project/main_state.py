from gfw import sprite
from pico2d import *
import json
import random

import gfw
from cookie import Cookie
from background import Background
from item import Item

class MainState:
    ITEM_P_COUNT = 2 # 아이템 패턴 개수

    def init(self):
        # self.bgm = load_music('./res/sound/bgm_gameplay.ogg')
        # self.bgm.repeat_play()
        
        self.background1 = Background('./res/bk/bk11-1.png', 2, 0.1, 2)
        self.background2 = Background('./res/bk/bk11-2.png', 3, 0.2, 2)
        self.background3 = Background('./res/bk/bk11-3.png', 2, 0.4, 2)
        self.background4 = Background('./res/bk/bk11-4.png', 2, 0.6, 2)
        self.tile = Background('./res/tile/tile11.png', 12, 3.0, 1)
        
        self.cookie = Cookie()

        self.items = []

        for i in range(5):
            objects = None
            with open('./res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json') as f:
                objects = json.load(f)

            for o in objects:
                self.items.append(Item(o, i * gfw.SCREEN_WIDTH))

    def update(self):
        self.cookie.update()
        self.background1.update()
        self.background2.update()
        self.background3.update()
        self.background4.update()
        self.tile.update()

        for i in self.items:
            i.update()

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()