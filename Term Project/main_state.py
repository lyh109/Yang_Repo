from gfw import SCREEN_HEIGHT, SCREEN_WIDTH, sprite
from pico2d import *
import json
import random

import gfw
from cookie import BraveCookie, Cookie, ZombieCookie
from background import Background
from object import Jelly, Tile, Obstacle, Dessert, Potion

class MainState:
    ITEM_P_COUNT = 4 # 아이템 패턴 개수

    def init(self):
        #self.bgm = load_music('./res/sound/bgm_gameplay.mp3')
        #self.bgm.repeat_play()

        self.game_over_sound = load_music('./res/sound/end.mp3')
        self.game_over_sound.set_volume(64)

        self.font = gfw.Text('./res/font.ttf', 32)
        self.font.x = SCREEN_WIDTH - 250.0
        self.font.y = SCREEN_HEIGHT - 60.0
        self.font.color_r = 0
        self.font.color_g = 0
        self.font.color_b = 0
        self.font.text = 'Score: 0'
        gfw.renderer.add_font(self.font)
        
        self.background1 = Background('./res/bk/bk6-1.png', 2, 400.0, 2)
        self.background2 = Background('./res/bk/bk6-2.png', 2, 450.0, 2)
        self.background3 = Background('./res/bk/bk6-3.png', 2, 480.0, 2)
        self.background4 = Background('./res/bk/bk6-4.png', 2, 550.0, 2)
        self.tile = Background('./res/stage/6/t0.png', 12, 450.0, 1)

        self.items = []
        self.tiles = []
        self.obstacles = []

        for i in range(10):
            objects = None
            #with open('./res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json') as f:
            with open('./res/data/objects4.json') as f:
                objects = json.load(f)

            for o in objects:
                if o['name'][0] == 'j':
                    self.items.append(Jelly(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 'd':
                    self.items.append(Dessert(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 'p':
                    self.items.append(Potion(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 't':
                    self.tiles.append(Tile(o, i * gfw.SCREEN_WIDTH))
                elif o['name'][0] == 'o':
                    self.obstacles.append(Obstacle(o, i * gfw.SCREEN_WIDTH))
                    

        self.cookie = ZombieCookie()

        self.hp_bar = gfw.Sprite('./res/hp_bar.jpg')
        self.hp_bar.x = 30.0
        self.hp_bar.y = SCREEN_HEIGHT - 42.0
        self.hp_bar.scale_x = 0.5
        self.hp_bar.scale_y = 0.5
        self.hp_bar.origin_x = 0.0
        self.hp_bar.origin_y = 1.0
        gfw.renderer.add(self.hp_bar)

        self.potion_0 = gfw.Sprite('./res/potion_0.png')
        self.potion_0.y = SCREEN_HEIGHT
        self.potion_0.origin_x = 0.0
        self.potion_0.origin_y = 1.0
        gfw.renderer.add(self.potion_0)

        self.hp = gfw.Sprite('./res/hp.png')
        self.hp.x = 70.0 # max: 535, min: 70.0
        self.hp.y = SCREEN_HEIGHT - 42.0
        self.hp.scale_x = 0.5
        self.hp.scale_y = 0.5
        self.hp.origin_x = 0.0
        self.hp.origin_y = 1.0
        gfw.renderer.add(self.hp)

        self.score = 0.0

    def update(self):
        cookie_left, cookie_right, cookie_bottom, cookie_top = self.cookie.get_col_box()
    
        self.cookie.hp - max(0.0, gfw.delta_time * 2.0)
        if self.cookie.hp > 0.0:
            self.background1.update()
            self.background2.update()
            self.background3.update()
            self.background4.update()
            self.tile.update()

            for i in self.items:
                if i.spr.active == False:
                    continue

                i.update()

                left, right, bottom, top = i.get_col_box()
                if cookie_left <= right and cookie_right >= left and cookie_bottom <= top and cookie_top >= bottom:
                    i.spr.active = False
                    i.ate_sound.play()

                    if type(i) == Potion:
                        self.cookie.hp = min(100.0, self.cookie.hp + i.hp)
                    else:
                        self.score += i.score

                draw_rectangle(left, bottom, right, top)

            for i in self.tiles:
                i.update()

            for i in self.obstacles:
                i.update()

                left, right, bottom, top = i.get_col_box()
                if cookie_left <= right and cookie_right >= left and cookie_bottom <= top and cookie_top >= bottom:
                    if self.cookie.cookie.alpha >= 1.0:
                        i.attack_sound.play()
                        if self.cookie.hit(10) == False:
                            self.game_over_sound.play()

                draw_rectangle(left, bottom, right, top)

            self.hp.x += (self.cookie.hp * (465.0 / 100) + 70.0 - self.hp.x) * 5.0 * gfw.delta_time
            self.score += gfw.delta_time * 2.0

        self.cookie.update(self.tiles)
        draw_rectangle(cookie_left, cookie_bottom, cookie_right, cookie_top)

        self.font.text = 'score: ' + str(int(self.score))
        
if __name__ == '__main__':
    gfw.init(MainState())
    gfw.run()