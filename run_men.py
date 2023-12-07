import arcade
import animation

class Run_men(animation.Animate):
    def __init__ (self,window):
        self.window=window
        super().__init__("runman/frame-01.gif",1.1)
        self.healf=5
        self.image_l=[]
        self.image_r=[]
        for i in range(1,10):
            self.image_l.append(arcade.load_texture(f"runman/frame-0{i}.gif"))
            self.image_r.append(arcade.load_texture(f"runman/frame-0{i}.gif",flipped_horizontally=True))
        self.napravlenie=True
        
    def update(self):
        if abs(self.center_x-self.window.bill.center_x)<600:
            if self.window.bill.center_x>self.center_x:
                self.textures=self.image_r
                self.change_x=1
            else:
                self.textures=self.image_l
                self.change_x=-1
        else:
            self.change_x=0