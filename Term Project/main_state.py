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

        self.objs = []

        for i in range(5):
            objects = None
            # with open('./res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json') as f:
            with open('./res/data/objects2.json') as f:
                objects = json.load(f)

            for o in objects:
                if o['name'][0] == 'j':
                    self.objs.append(Jelly(o, i * gfw.SCREEN_WIDTH))
                else:
                    self.objs.append(Tile(o, i * gfw.SCREEN_WIDTH))

    def update(self):
        self.cookie.update()
        self.background1.update()
        self.background2.update()
        self.background3.update()
        self.background4.update()
        self.tile.update()

        cookie_col_left = self.cookie.col_box_x - self.cookie.col_box_w * 0.5
        cookie_col_right = self.cookie.col_box_x + self.cookie.col_box_w * 0.5
        cookie_col_bottom= self.cookie.col_box_y - self.cookie.col_box_h * 0.5
        cookie_col_top= self.cookie.col_box_y + self.cookie.col_box_h * 0.5

        for i in self.objs:
            if i.spr.active == False:
                continue

            i.update()

            left = i.col_box_x - i.col_box_w * 0.5
            right = i.col_box_x + i.col_box_w * 0.5
            bottom = i.col_box_y - i.col_box_h * 0.5
            top = i.col_box_y + i.col_box_h * 0.5

            if type(i) == Jelly:
                if cookie_col_left <= right and cookie_col_right >= left and cookie_col_bottom <= top and cookie_col_top >= bottom:
                    i.spr.active = False
                    i.ate_sound.play()

            draw_rectangle(left, bottom, right, top)
        
        draw_rectangle(cookie_col_left, cookie_col_bottom, cookie_col_right, cookie_col_top)
        

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()