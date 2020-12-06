from pico2d import *
import time
import gfw.events_handler as eh
from gfw.renderer import Renderer
from gfw.sprite import Sprite
from gfw.text import Text

FPS = 60.0

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 640

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
    global states
    
    while running:
        start_time = time.time()

        if eh.update() == False:
            break

        # states[0].update()

        clear_canvas()
        renderer.draw()
        states[-1].update()
        update_canvas()
        
        delay_time = 1 / FPS - (time.time() - start_time)
        if delay_time > 0.0:
            delay(delay_time)

        delta_time = time.time() - start_time

    while states:
        states[-1].exit()
        states.pop()

    close_canvas()

def quit():
    global running
    running = False

def change_state(state):
    global states

    if states:
        states[-1].exit()
        states.pop()

    states.append(state)
    state.init()

def push_state(state):
    global states

    if states:
        states[-1].pause()

    states.append(state)
    state.init()

def pop_state():
    global states

    if len(states) > 1:
        states[-1].exit()
        states.pop()

        states[-1].resume()
    else:
        quit()