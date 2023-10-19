import arcade

class Animate(arcade.Sprite):
    time_texture=0
    index=0
    def update_animation(self, delta_time: float = 1 / 60):
        self.time_texture+=delta_time
        if self.time_texture>0.1:
            self.time_texture=0
            if self.index==len(self.textures)-1:
                self.index=0
            else:
                self.index+=1
            self.set_texture(self.index)