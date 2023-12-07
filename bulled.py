import arcade
from settings import *


class Pula(arcade.Sprite):
    def __init__(self,window):
        super().__init__("bullet.png",0.03)
        self.window=window
        if self.window.bill.side:
            self.change_x=-SPEED_BULLED
        else:
            self.change_x=SPEED_BULLED
    def update(self):
        self.center_x+=self.change_x
        if self.center_x>WIDHT and self.center_x<0:
            self.kill()
class Shut(Pula):
    def __init__(self,window,x,y,change_x,change_y):
        super().__init__(window)
        self.change_x=change_x
        self.change_y=change_y
        self.set_position(x,y)
        
    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.center_x>WIDHT and self.center_x<0:
            self.kill()
        
        