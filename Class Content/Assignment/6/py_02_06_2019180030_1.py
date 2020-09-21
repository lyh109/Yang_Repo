from pico2d import *
from helper import *

RES_DIR = '../res'

open_canvas()


class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = 100, 85
        self.dx, self.dy = 0, 0
        self.fidx = 0
        self.speed = 1
        self.tx, self.ty = 100, 85
        self.image = load_image(RES_DIR + '/run_animation.png')

    def draw(self):
        self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.fidx = (self.fidx + 1) % 8


grass = Grass()
boy = Boy()
click = 0
path = []


def handle_events():
    global running, click, path
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            path.append((e.x, 600 - 1 - e.y))
            (boy.tx, boy.ty) = path[0]
            if click > 0:
                boy.speed += 1
            click += 1


running = True
done = False

while running:
    clear_canvas()

    grass.draw()
    boy.draw()

    update_canvas()

    handle_events()

    (boy.dx, boy.dy) = delta((boy.x, boy.y), (boy.tx, boy.ty), boy.speed)
    ((boy.x, boy.y), done) = move_toward((boy.x, boy.y), (boy.dx, boy.dy), (boy.tx, boy.ty))

    if done is True:
        done = False

        if len(path) > 1:
            (boy.tx, boy.ty) = path[1]
            path.remove(path[0])
        else:
            boy.speed = 1
            click = 0

    grass.update()
    boy.update()

    delay(0.02)

close_canvas()
