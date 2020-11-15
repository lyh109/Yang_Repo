import gfw

class Background:
    def __init__(self, image_path):
        self.repeat_count = 0
        self.speed = 0.0

        self.back_pieces = [ gfw.Sprite(image_path), gfw.Sprite(image_path) ] # TODO: repeat만큼 loop 돌리자
        for i in range(0, self.repeat_count):
            self.back_pieces[i].scale_x = 2.0
            self.back_pieces[i].scale_y = 2.0
            self.back_pieces[i].origin_x = -i
            self.back_pieces[i].origin_y = 0.0
            gfw.renderer.add(self.back_pieces[i])

    def update(self):
        for i in self.back_pieces:
            i.origin_x += gfw.delta_time * 0.5
            if i.origin_x >= 1.0:
                i.origin_x -= 2.0