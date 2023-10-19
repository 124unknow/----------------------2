import arcade
from animation import Animate
from settings import *

class Bill (Animate):
    def __init__(self,window):
        super().__init__("go_bill/0.gif",1.1)    
        self.list_right=[]
        self.list_left=[]
        self.center_x=100
        self.center_y=100
        self.wolk=True
        self.down_r=arcade.load_texture("bill_textures/BillLayingDown.png")
        self.down_l=arcade.load_texture("bill_textures/BillLayingDown.png",flipped_horizontally=True)
        for i in range(6):
            self.list_right.append(arcade.load_texture(f"go_bill/{i}.gif"))
            self.list_left.append(arcade.load_texture(f"go_bill/{i}.gif",flipped_horizontally=True))
        self.side=True
    
    def down(self):
        if self.side==True:
            self.texture=self.down_l
        else:
            self.texture=self.down_r

    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
    
    def get_side(self):
        if self.side:
            self.textures=self.list_left
        else:
            self.textures=self.list_right

    
    def update_animation(self, delta_time: float = 1 / 60):
        if self.wolk:
            super().update_animation(delta_time)
    
    def come_left(self):
        if self.left>WIDHT:
            self.center_x=0
            return True
        return False
    
    def come_right(self):
        if self.right<0:
            self.center_x=WIDHT
            return True
        return False
