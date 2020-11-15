from pico2d import *

def handle_events():
    global running
    global dx

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dx += 1
            elif event.key == SDLK_LEFT:
                dx -=1
            elif event.key == SDLK_ESCAPE:
                running = False



open_canvas()

gra = load_image('../res/grass.png')
ch = load_image('../res/character.png')

running = True
x = 400
dx = 0
fidx = 0

