from pico2d import *
import gfw

class Background:
    def __init__(self, image_path, repeat_count, speed, scale, ):
        self.speed = speed
        self.repeat_count = repeat_count

        self.back_pieces = [  gfw.Sprite(image_path) for i in range(repeat_count) ]
        for i in range(0, repeat_count):
            self.back_pieces[i].scale_x = scale
            self.back_pieces[i].scale_y = scale
            self.back_pieces[i].origin_x = -i
            self.back_pieces[i].origin_y = 0.0
            gfw.renderer.add(self.back_pieces[i])

    def update(self):
        for i in self.back_pieces:
            i.origin_x += gfw.delta_time * self.speed
            if i.origin_x >= 1.0:
                i.origin_x -= self.repeat_count