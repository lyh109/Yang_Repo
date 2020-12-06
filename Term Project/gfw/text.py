from pico2d import *

class Text:
    def __init__(self, ttf_path, size):
        self.x = 0.0
        self.y = 0.0
        self.color_r = 255
        self.color_g = 255
        self.color_b = 255
        self.text = ''
        self.ttf = load_font(ttf_path, size)