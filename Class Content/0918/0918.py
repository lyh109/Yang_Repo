from pico2d import *
from gobj import *


def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False


open_canvas()

grass = Grass()
# boy = Boy()
team = [Boy() for i in range(11)]

running = True
while running:
    clear_canvas()
    grass.draw()
    # boy.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    handle_events()

    grass.update()
    # boy.update()
    for boy in team:
        boy.update()

    delay(0.03)

close_canvas()
