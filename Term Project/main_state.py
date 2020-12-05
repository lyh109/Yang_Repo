from gfw import sprite
from pico2d import *
import json
import random

import gfw
from cookie import Cookie
from background import Background
from object import Jelly, Tile

class MainState:
    ITEM_P_COUNT = 2 # 아이템 패턴 개수

    def init(self):
        self.bgm = load_music('./res/sound/bgm_gameplay.ogg')
        self.bgm.repeat_play()
        
        self.background1 = Background('./res/bk/bk11-1.png', 2, 0.1, 2)
        self.background2 = Background('./res/bk/bk11-2.png', 3, 0.2, 2)
        self.background3 = Background('./res/bk/bk11-3.png', 2, 0.4, 2)
        self.background4 = Background('./res/bk/bk11-4.png', 2, 0.6, 2)
        self.tile = Background('./res/stage/11/t0.png', 12, 3.0, 1)
        
        self.cookie = Cookie()

        self.jellies = []
        self.tiles = []

        for i in range(5):
            objects = None
            # with open('./res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json') as f:
            with open('./res/data/objects2.json') as f:
                objects = json.load(f)

            for o in objects:
                if o['name'][0] == 'j':
                    self.jellies.append(Jelly(o, i * gfw.SCREEN_WIDTH))
                else:
                    self.tiles.append(Tile(o, i * gfw.SCREEN_WIDTH))

    def update(self):
        self.background1.update()
        self.background2.update()
        self.background3.update()
        self.background4.update()
        self.tile.update()

        cookie_left, cookie_right, cookie_bottom, cookie_top = self.cookie.get_col_box()

        for i in self.jellies:
            if i.spr.active == False:
                continue

            i.update()

            left, right, bottom, top = i.get_col_box()
            if cookie_left <= right and cookie_right >= left and cookie_bottom <= top and cookie_top >= bottom:
                i.spr.active = False
                i.ate_sound.play()

            draw_rectangle(left, bottom, right, top)

        for i in self.tiles:
            i.update()
        
        self.cookie.update(self.tiles)
        draw_rectangle(cookie_left, cookie_bottom, cookie_right, cookie_top)
        

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()