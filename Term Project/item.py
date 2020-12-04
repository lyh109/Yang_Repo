import gfw

class Item:
    def __init__(self, data, offsetX):
        self.frame_count = 0
        self.kind = int(data['name'][1])

        if data['name'] == 'j0' or data['name'] == 'j1':
            self.spr = gfw.Sprite('./res/basic_jellies.png')
            self.frame_count = 3
            self.spr.cell_image_width = 38
            self.spr.cell_index_x = self.kind * self.frame_count
        else:
            self.spr = gfw.Sprite('./res/bear_jellies.png')
            if self.kind % 2 == 0:
                self.frame_count = 1
            else:
                self.frame_count = 2

            if self.kind == 2:
                self.spr.cell_index_x = 0
            elif self.kind == 3:
                self.spr.cell_index_x = 1
            elif self.kind == 4:
                self.spr.cell_index_x = 3
            elif self.kind == 5:
                self.spr.cell_index_x = 4
            elif self.kind == 6:
                self.spr.cell_index_x = 6
            elif self.kind == 7:
                self.spr.cell_index_x = 7
            elif self.kind == 8:
                self.spr.cell_index_x = 9
            elif self.kind == 9:
                self.spr.cell_index_x = 10

            self.spr.cell_image_width = 55
        
        self.spr.cell_image_height = 51       
        self.spr.x = data["x"] + offsetX
        self.spr.y = data["y"]
        self.spr.is_clip_image = True
        self.spr.padding_size = 2
        self.spr.cell_index_y = 0
        gfw.renderer.add(self.spr)

        self.score = 0.0

    def update(self):
        self.spr.x -= 200.0 * gfw.delta_time