from pico2d import *
import time
import gfw.events_handler as eh
from gfw.renderer import Renderer
from gfw.sprite import Sprite

FPS = 60.0

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

running = True
delta_time = 0.0
states = []
renderer = None

def init(state):
    global renderer

    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    renderer = Renderer()
    
    states.append(state)
    state.init()

def run():
    global running
    global delta_time
    
    while running:
        start_time = time.time()

        if eh.update() == False:
            break

        states[0].update()

        clear_canvas()
        renderer.draw()
        update_canvas()
        
        delay_time = 1 / FPS - (time.time() - start_time)
        if delay_time > 0.0:
            delay(delay_time)

        delta_time = time.time() - start_time

    close_canvas()