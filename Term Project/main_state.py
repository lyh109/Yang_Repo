from score_state import ScoreState
from gfw import SCREEN_HEIGHT, SCREEN_WIDTH, sprite
from gfw.events_handler import LBUTTON
from pico2d import *
import json
import random

import gfw
from cookie import BraveCookie, Cookie, ZombieCookie
from background import Background
from object import Jelly, Tile, Obstacle, Dessert, Potion

class MainState:
    ITEM_P_COUNT = 6 # 아이템 패턴 개수
    def __init__(self, cookie_type):
        self.cookie_type = cookie_type

    def init(self):
        self.start = False
        self.stop_game = False
        self.bgm = load_music('./res/sound/bgm_gameplay.mp3')
        self.bgm.repeat_play()

        self.game_over_sound = load_music('./res/sound/end.mp3')
        self.game_over_sound.set_volume(64)

        self.select_button_sound = load_wav('./res/sound/button_off.wav')

        self.font = gfw.Text('./res/font.ttf', 32)
        self.font.x = SCREEN_WIDTH - 250.0
        self.font.y = SCREEN_HEIGHT - 60.0
        self.font.color_r = 0
        self.font.color_g = 0
        self.font.color_b = 0
        self.font.text = 'SCORE: 0'
        gfw.renderer.add_font(self.font)
        
        self.background1 = Background('./res/bk/bk6-1.png', 2, 400.0, 2)
        self.background2 = Background('./res/bk/bk6-2.png', 2, 450.0, 2)
        self.background3 = Background('./res/bk/bk6-3.png', 2, 480.0, 2)
        self.background4 = Background('./res/bk/bk6-4.png', 2, 550.0, 2)
        self.tile = Background('./res/stage/6/t0.png', 12, 450.0, 1)

        self.items = []
        self.tiles = []
        self.obstacles = []

        object_datas = {}

        for i in range(50):
            objects = None
            if self.start == False:
                with open('./res/data/objects0.json') as f:
                    objects = json.load(f)
                    self.start = True
            else:
                path = './res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json'

                if not path in object_datas:
                    with open('./res/data/objects' + str(random.randrange(0, self.ITEM_P_COUNT)) + '.json') as f:
                        object_datas[path] = json.load(f)

                objects = object_datas[path]

            for o in objects:
                obj_first_name = o['name'][0]
                if obj_first_name == 'j':
                    self.items.append(Jelly(o, i * gfw.SCREEN_WIDTH))
                elif obj_first_name == 'd':
                    self.items.append(Dessert(o, i * gfw.SCREEN_WIDTH))
                elif obj_first_name == 'p':
                    self.items.append(Potion(o, i * gfw.SCREEN_WIDTH))
                elif obj_first_name == 't':
                    self.tiles.append(Tile(o, i * gfw.SCREEN_WIDTH))
                elif obj_first_name == 'o':
                    self.obstacles.append(Obstacle(o, i * gfw.SCREEN_WIDTH))
                    
        self.cookie = None
        if self.cookie_type == 0:
            self.cookie = BraveCookie()
        else:
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

        self.black_screen = gfw.Sprite('./res/bk/bb.png')
        self.black_screen.x = gfw.SCREEN_WIDTH * 0.5
        self.black_screen.y = gfw.SCREEN_HEIGHT * 0.5
        self.black_screen.alpha = 0.0
        self.black_screen.active = False
        gfw.renderer.add(self.black_screen)

        self.resume_button = gfw.Sprite('./res/resume_button.png')
        self.resume_button.x = SCREEN_WIDTH * 0.5 - 180.0
        self.resume_button.y = SCREEN_HEIGHT * 0.5
        self.resume_button.active = False
        gfw.renderer.add(self.resume_button)

        self.exit_button = gfw.Sprite('./res/exit_button.png')
        self.exit_button.x = SCREEN_WIDTH * 0.5 + 180.0
        self.exit_button.y = SCREEN_HEIGHT * 0.5
        self.exit_button.active = False
        gfw.renderer.add(self.exit_button)

        self.score = 0.0

    def update(self):
        mouse_x, mouse_y = gfw.eh.mouse_pos[0],  gfw.eh.mouse_pos[1]
        r_button_half_w = self.resume_button.image.w * 0.5
        r_button_half_h = self.resume_button.image.h * 0.5

        if self.resume_button.x - r_button_half_w <= mouse_x and mouse_x <= self.resume_button.x + r_button_half_w and self.resume_button.y - r_button_half_h <= mouse_y and mouse_y < self.resume_button.y + r_button_half_h:
            self.resume_button.scale_x = 1.2
            self.resume_button.scale_y = 1.2
            if gfw.eh.get_mouse_button_down(LBUTTON):
                self.resume_button.active = False
                self.exit_button.active = False
                self.black_screen.active = False
                self.black_screen.alpha = 0.0
                self.stop_game = False
        else:
            self.resume_button.scale_x = 1.0
            self.resume_button.scale_y = 1.0

        if self.exit_button.x - r_button_half_w <= mouse_x and mouse_x <= self.exit_button.x + r_button_half_w and self.exit_button.y - r_button_half_h <= mouse_y and mouse_y < self.exit_button.y + r_button_half_h:
            self.exit_button.scale_x = 1.2
            self.exit_button.scale_y = 1.2
            if gfw.eh.get_mouse_button_down(LBUTTON):
                gfw.pop_state()
        else:
            self.exit_button.scale_x = 1.0
            self.exit_button.scale_y = 1.0
        
        if self.stop_game:
            return

        cookie_left, cookie_right, cookie_bottom, cookie_top = self.cookie.get_col_box()
    
        if self.cookie.hp > 0.0:
            self.cookie.hp = max(0.0, self.cookie.hp - gfw.delta_time * 5.0)
            if self.cookie.hp <= 0.0:
                if type(self.cookie) == ZombieCookie and self.cookie.life > 0:
                    self.cookie.hp += 10 * self.cookie.life
                    self.cookie.life -= 1
                else:
                    self.game_over_sound.play()
                    self.black_screen.active = True

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

                # draw_rectangle(left, bottom, right, top)

            for i in self.tiles:
                i.update()

            for i in self.obstacles:
                i.update()

                left, right, bottom, top = i.get_col_box()
                if cookie_left <= right and cookie_right >= left and cookie_bottom <= top and cookie_top >= bottom:
                    if self.cookie.cookie.alpha >= 1.0:
                        i.attack_sound.play()
                        if self.cookie.hit(10) == False:
                            if type(self.cookie) == ZombieCookie and self.cookie.life > 0:
                                self.cookie.hp += 10 * self.cookie.life
                                --self.cookie.life
                            else:
                                self.game_over_sound.play()

                # draw_rectangle(left, bottom, right, top)

            self.hp.x += (self.cookie.hp * (465.0 / 100) + 70.0 - self.hp.x) * 5.0 * gfw.delta_time
            self.hp_bar.image.w += (self.cookie.hp * (465.0 / 100) + 40 - (self.hp_bar.image.w * 0.5)) * 5.0 * gfw.delta_time
            self.score += gfw.delta_time * 2.0
        else:
            self.black_screen.active = True
            if self.black_screen.active:
                self.black_screen.alpha = min(1.0, self.black_screen.alpha + gfw.delta_time * 2.0)
            if self.black_screen.alpha >= 1.0:
                gfw.push_state(ScoreState(self.score))

        self.cookie.update(self.tiles)
        # draw_rectangle(cookie_left, cookie_bottom, cookie_right, cookie_top)

        self.font.text = 'SCORE: ' + str(int(self.score))

        if gfw.eh.get_key_down(gfw.SDLK_ESCAPE):
            self.stop_game = True
            self.resume_button.active = True
            self.exit_button.active = True
            self.black_screen.active = True
            self.black_screen.alpha = 0.5

    def pause(self):
        pass

    def resume(self):
        pass

    def exit(self):
        gfw.renderer.clear()
        
if __name__ == '__main__':
    gfw.init(MainState(0))
    gfw.run()