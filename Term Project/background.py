from pico2d import *
import gfw

class Background:
    def __init__(self, image_path, repeat_count, speed, scale):
        self.speed = speed
        self.repeat_count = repeat_count

        self.back_pieces = [  gfw.Sprite(image_path) for i in range(repeat_count) ]
        for i in range(0, repeat_count):
            piece = self.back_pieces[i]
            piece.scale_x = scale
            piece.scale_y = scale
            piece.x = i * piece.image.w * piece.scale_x
            piece.origin_x = 0.0
            piece.origin_y = 0.0
            gfw.renderer.add(piece)            

    def update(self):
        for i in self.back_pieces:
           i.x -= gfw.delta_time * self.speed

           final_w = i.image.w * i.scale_x
           if i.x + final_w < 0.0:
               i.x += self.repeat_count * final_w

        #for i in self.back_pieces:
        #    i.origin_x += gfw.delta_time * self.speed
        #    if i.origin_x >= 1.0:
        #        i.origin_x -= self.repeat_count