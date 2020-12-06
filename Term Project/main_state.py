from gfw import sprite
from pico2d import *
import json
import random

import gfw
from cookie import Cookie
from background import Background
from object import Jelly, Tile, Obstacle, Dessert

class MainState:
    ITEM_P_COUNT = 4 # 아이템 패턴 개수

    def init(self):
        self.bgm = load_music('./res/sound/bgm_gameplay.mp3')
        self.bgm.repeat_play()
        
        self.background1 = Background('./res/bk/bk6-1.png', 2, 0.1, 2)
        self.background2 = Background('./res/bk/bk6-2.png', 3, 0.2, 2)
        self.background3 = Background('./res/bk/bk6-3.png', 2, 0.4, 2)
        self.background4 = Background('./res/bk/bk6-4.png', 2, 0.6, 2)
        self.tile = Background('./res/stage/6/t0.png', 12, 3.0, 1)

        self.jellies = []
        self.tiles = []
        self.obstacles = []

        for i in range(5):
            objects = None
            # with open('./res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json') as f:
            with open('./res/data/objects4.json') as f:
                objects = json.load(f)

            for o in objects:
                if o['name'][0] == 'j':
                    self.jellies.append(Jelly(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 'd':
                    self.jellies.append(Dessert(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 't':
                    self.tiles.append(Tile(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 'o':
                    self.obstacles.append(Obstacle(o, i * gfw.SCREEN_WIDTH))
                    
        self.cookie = Cookie()

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

        for i in self.obstacles:
            left, right, bottom, top = i.get_col_box()
            i.update()
            draw_rectangle(left, bottom, right, top)
        
        self.cookie.update(self.tiles)
        draw_rectangle(cookie_left, cookie_bottom, cookie_right, cookie_top)
        

if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()