import gfw

ACC = 0.1

class Cookie:
    def __init__(self):
        self.cookie = gfw.Sprite('./res/Brave_Cookie.png')
        self.cookie.is_clip_image = True
        self.cookie.padding_size = 2
        self.cookie.cell_image_width = 270
        self.cookie.cell_image_height = 270
        self.cookie.cell_index_x = 1
        self.cookie.cell_index_y = 4
        self.cookie.scale_x = 1.0
        self.cookie.scale_y = 1.0
        self.cookie.x = 100.0
        self.cookie.y = 200.0        
        gfw.renderer.add(self.cookie)

        self.acc = 0.0
        self.elapsed_time = 0.0
        self.speedY = 0.0
        self.state = 0

    def update(self):
        self.speedY -= ACC
        self.cookie.y += self.speedY

        if self.cookie.y <= 200.0:
            self.cookie.y = 200.0
            self.speedY = 0.0
            self.state = 0

        if gfw.eh.get_key_down(gfw.SDLK_SPACE):
            if self.state < 2:
                self.speedY = 7.0
                self.state += 1
                self.cookie.cell_index_x = 1
        elif gfw.eh.get_key(gfw.SDLK_DOWN):
            self.state = -1
        

        # Update animation
        self.elapsed_time += gfw.delta_time

        if self.elapsed_time >= 0.07:
            if self.state == 0:
                self.cookie.cell_index_x = int(self.cookie.cell_index_x + 1) % 4
                self.cookie.cell_index_y = 4
            elif self.state == 1:
                self.cookie.cell_index_x = 7
                self.cookie.cell_index_y = 5
            elif self.state == 2:
                self.cookie.cell_index_x = int(self.cookie.cell_index_x + 1) % 6
                self.cookie.cell_index_y = 5
            elif self.state == -1:
                self.cookie.cell_index_x = 9
                self.cookie.cell_index_y = 5
            self.elapsed_time = 0.0

        print(self.state)