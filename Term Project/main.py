from pico2d import *

SCREEN_WIDTH = 1136
SCREEN_HEIGHT = 636

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False

open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)

flow = 0
nf = 0
stage = 0

images = [load_image('res/stage1.png'), load_image('res/stage2.png'), load_image('res/stage3.png')]
cur_image = images[stage]

black_screen = load_image('res/bb.png')
alpha = 0.0
alpha_up = True
run = True

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
            if alpha >= 1.0:
               alpha_up = False 
               alpha = 1.0
               if stage < len(images) - 1:
                    stage += 1
               cur_image = images[stage]
        else:
            alpha -= 0.001
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
            if nf % 4 == 0:
                nf = 0
                flow = 0
                if stage < len(images) - 1:
                    run = False

    print(flow)

    update_canvas()

close_canvas()