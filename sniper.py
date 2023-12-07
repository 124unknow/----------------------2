import arcade
import time
from bulled import Shut

class R_bill(arcade.Sprite):
    def __init__(self,window):
        super().__init__("sniper/sniper_angle.png",1.1)
        self.window=window
        self.healf=4
        self.leftt=arcade.load_texture(f"sniper/sniper_forward.png")
        self.rightt=arcade.load_texture(f"sniper/sniper_forward.png",flipped_horizontally=True)
        self.l_angle=arcade.load_texture(f"sniper/sniper_angle.png")
        self.r_angle=arcade.load_texture(f"sniper/sniper_angle.png",flipped_horizontally=True)
        self.last_shooting_time=time.time()
    def update(self):
        if self.center_y>self.window.bill.center_y:
            if self.center_x>self.window.bill.center_x:
                self.texture=self.l_angle
                self.shooting(-10,-10)
            else:
                self.texture=self.r_angle
                self.shooting(10,-10)

        else:
            if self.center_x>self.window.bill.center_x:
                self.texture=self.leftt
                self.shooting(-10,0)
            else:
                self.texture=self.rightt
                self.shooting(10,0)
    def shooting(self,change_x,change_y):
        if time.time()-self.last_shooting_time>2:
            list_pula=Shut(self.window,self.center_x,self.center_y,change_x,change_y)
            self.window.shoot.append(list_pula)
            self.last_shooting_time=time.time()
        