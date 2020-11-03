from pico2d import *

SCREEN_WIDTH = 1136
SCREEN_HEIGHT = 636

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

class Cookie:
    ACTIONS = ['Run', 'Jump', 'Double Jump', 'Bump', 'Dead']
    def __init__(self):
        self.x, self.y = 150, 208
        self.image = load_image('res/Brave_Cookie.png')
        self.action = 0
        self.speed = 50
        self.dx = 2.5
        self.fidx = 0
        self.fidy = 2

Player = Cookie()

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_DOWN:
                Player.action = 0
                Player.fidx = 0
                Player.fidy = 2
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_SPACE:
                Player.action = 1
                Player.fidx = 0
                Player.fidy = 6
            elif e.key == SDLK_DOWN:
                Player.action = 2
                Player.fidx = 10
                Player.fidy = 1
        
flow = 0
nf = 0
stage = 0

images = [load_image('res/stage1.png'), load_image('res/stage2.png'), load_image('res/stage3.png')]
cur_image = images[stage]

black_screen = load_image('res/bb.png')
alpha = 0.0
alpha_up = True
run = True

jump_up = True

while True:
    handle_events()

    clear_canvas()

    for i in range(0, 2):
        x = cur_image.w / 2 + (cur_image.w * i) - flow
        y = cur_image.h / 2
        cur_image.draw(x, y) 

    if not run:
        if alpha_up:
            alpha += 0.001

            Player.x += Player.dx
            Player.image.clip_draw(2 + (Player.fidx * 272), 1634 - (Player.fidy * 272), 270, 270, Player.x, Player.y, 180, 180)
            if Player.action == 0:
                Player.fidx = (Player.fidx + 1) % 4
            elif Player.action == 1:
                if Player.y % 20 == 0:
                    Player.fidx = (Player.fidx + 1) % 5
                if jump_up:
                    Player.y += 1
                    if Player.y >= 308:
                        jump_up = False
                else:
                    Player.y -= 1
                    if Player.y <= 208:
                        jump_up = True
                        Player.action = 0
                        Player.fidx = 0
                        Player.fidy = 2
            elif Player.action == 2:
                pass
            
            if alpha >= 1.0:
               alpha_up = False 
               alpha = 1.0
               if stage < len(images) - 1:
                    stage += 1
               cur_image = images[stage]
               Player.x = -270
               Player.y = 208
        else:
            alpha -= 0.001

            Player.image.clip_draw(2 + (Player.fidx * 272), 1634 - (Player.fidy * 272), 270, 270, Player.x, Player.y, 180, 180)
            if Player.action == 0:
                Player.fidx = (Player.fidx + 1) % 4
                if Player.x < 150:
                    Player.x += 0.4
            elif Player.action == 1:
                if Player.y % 20 == 0:
                    Player.fidx = (Player.fidx + 1) % 5
                if jump_up:
                    Player.y += 1
                    if Player.y >= 308:
                        jump_up = False
                else:
                    Player.y -= 1
                    if Player.y <= 208:
                        jump_up = True
                        Player.action = 0
                        Player.fidx = 0
                        Player.fidy = 2      
            elif Player.action == 2:
                pass
            
            
            if alpha <= 0.0:
                alpha_up = True
                run = True
        
        black_screen.opacify(alpha)
        black_screen.draw(black_screen.w / 2, black_screen.h / 2)

    if run:
        flow += 5
        if flow >= cur_image.w:
            flow = 0
            nf += 1
            if (nf + stage) % 4  == 0:
                nf = 0
                flow = 0
                if stage < len(images) - 1:
                    run = False

        Player.image.clip_draw(2 + (Player.fidx * 272), 1634 - (Player.fidy * 272), 270, 270, Player.x, Player.y, 180, 180)
        if Player.x < 150:
            Player.x += 0.4
        
        if Player.action == 0:
            Player.fidx = (Player.fidx + 1) % 4
        elif Player.action == 1:
            if Player.y % 20 == 0:
                Player.fidx = (Player.fidx + 1) % 5
            if jump_up:
               Player.y += 1
               if Player.y >= 308:
                   jump_up = False
            else:
               Player.y -= 1
               if Player.y <= 208:
                   jump_up = True
                   Player.action = 0
                   Player.fidx = 0
                   Player.fidy = 2
        elif Player.action == 2:
            pass

    update_canvas()

close_canvas()

# 스테이트 분리하기
# 점프 이미지 수정
# 배경 여러 이미지가 다른 속도로 흘러가도록 수정
# 다른 쿠키 이미지 추가
# 다른 플레이어블 쿠키를 먼저 만들고, 이후에 장애물 추가 (일정 순서 변경)
# 지금은 세 개의 스테이지로 아루어져 있는데, 추가 스테이지를 만들 수 있도록 함
# 체력바 이미지 찾기