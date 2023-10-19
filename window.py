import arcade
from settings import *
import os
from bulled import Pula 
from player_bill import Bill 
from platforma import Platforma
from coords import *



path=os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


class Window (arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.background=[]
        for i in range(1,16):
            self.background.append(arcade.load_texture(f"background/Map{i}.png"))
        self.index_texture=0
        self.pula=arcade.SpriteList()
        self.status_game=True
        self.bill=Bill(self)
        self.platforms=arcade.SpriteList()
        self.settings()
        self.physics_engines=arcade.PhysicsEnginePlatformer(self.bill,self.platforms,GRAVIT)
        self.platforms_for_lvl=[]

    def on_draw(self):
        arcade.draw_texture_rectangle(WIDHT/2,HEIGHT/2,WIDHT,HEIGHT,self.background[self.index_texture])
        self.pula.draw()
        self.bill.draw()
        self.platforms.draw()

    def update(self,delta_time):
        self.pula.update()
        self.bill.update()
        self.bill.update_animation()
        self.physics_engines.update()
        if self.bill.come_left():
            if self.index_texture<len(self.background)-2:
                self.index_texture+=1
        elif self.bill.come_right():
            if self.index_texture>0:
                self.index_texture-=1


    def settings(self):
        for i in range(0,801,100):
            platforma=Platforma()
            platforma.set_position(i,20)
            self.platforms.append(platforma)
        for q,w in enumerate(COORDS):
            print(q,w)


    def on_key_press (self, symbol: int, modifiers: int):
        if symbol==arcade.key.E:
            self.pulaa=Pula()
            self.pula.append(self.pulaa)
        if symbol==arcade.key.A:
            self.bill.change_x=-5
            self.bill.wolk=True
            self.bill.side=True
            self.bill.get_side()
        if symbol==arcade.key.D:
            self.bill.change_x=5
            self.bill.wolk=True
            self.bill.side=False
            self.bill.get_side()
        if symbol==arcade.key.SPACE:
            self.bill.down()
        if symbol==arcade.key.W and self.physics_engines.can_jump():
            self.physics_engines.jump(POWER_UP)
        
    

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol==arcade.key.A or  symbol==arcade.key.D:
            self.bill.change_x=0
            self.bill.wolk=False


lon=Window(WIDHT,HEIGHT,TITLE)
arcade.run()