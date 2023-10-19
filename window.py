import arcade
from settings import *
import os
from bulled import Pula 
from player_bill import Bill 
from platforma import Platforma



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
        self.physics_engines=arcade.PhysicsEnginePlatformer(self.bill,self.platforms,GRAVIT)

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

    def settings(self):
        for i in range(0,801,100):
            pass


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
    

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol==arcade.key.A or  symbol==arcade.key.D:
            self.bill.change_x=0
            self.bill.wolk=False


lon=Window(WIDHT,HEIGHT,TITLE)
arcade.run()