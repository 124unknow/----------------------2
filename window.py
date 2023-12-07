import arcade
from settings import *
import os
from bulled import Pula 
from player_bill import Bill 
from platforma import Platforma
from coords import *
from run_men import Run_men
import random
from sniper import*



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
        self.platforms_for_lvl=[]
        self.run_man=arcade.SpriteList()
        self.run_man_for_lvl=[]
        self.run_man_enjay=[]
        self.list_sn=arcade.SpriteList()
        self.sniper_for_lvl=[]
        self.settings()
        self.jump=arcade.load_sound("sounds/jump.wav")
        self.shoot=arcade.load_sound("sounds/shoot.wav")
        self.physics_engines=arcade.PhysicsEnginePlatformer(self.bill,self.platforms,GRAVIT)
        

    def on_draw(self):
        arcade.draw_texture_rectangle(WIDHT/2,HEIGHT/2,WIDHT,HEIGHT,self.background[self.index_texture])
        self.pula.draw()
        self.bill.draw()
        self.platforms.draw()
        self.run_man.draw()
        self.list_sn.draw()

    def update(self,delta_time):
        self.pula.update()
        self.bill.update()
        self.bill.update_animation()
        self.physics_engines.update()
        self.list_sn.update()

        if self.bill.come_left():
            if self.index_texture<len(self.background)-2:
                self.index_texture+=1
                self.append_and_kill_platforms(-1)
        elif self.bill.come_right():
            if self.index_texture>0:
                self.index_texture-=1
                self.append_and_kill_platforms(1)
        self.run_man.update()
        self.run_man.update_animation()
        for dvigat in self.run_man_enjay:#сделать так чтобы боты смотрели на тебя при обгоне
            dvigat.update()
            


    def settings(self):
        for i in range(0,801,100):
            platforma=Platforma()
            platforma.set_position(i,20)
            self.platforms.append(platforma)
        for q,w in enumerate(COORDS):
            self.platforms_for_lvl.append([]) 
            self.run_man_for_lvl.append([])
            for x,y in w:
                qw_platforma=Platforma()
                qw_platforma.set_position(x,y)
                self.platforms_for_lvl[q].append(qw_platforma)
                run_men=Run_men(self)
                if x < 0 :
                    run_men.set_position(x,y+40)
                else:
                    run_men.set_position(random.randint(100,WIDHT-100),100)
                self.run_man_for_lvl[q].append(run_men)
        for q,w in enumerate(COORDS_SN):
            self.sniper_for_lvl.append([])
            for x,y in w:
                qw_sniper=R_bill(self)
                qw_sniper.set_position(x,y)
                self.sniper_for_lvl[q].append(qw_sniper)

        self.append_and_kill_platforms(0)
        
    
    def append_and_kill_platforms(self,sayd):
        self.append_and_kill_people(sayd)
        self.append_and_kill_snipers(sayd)
        if sayd :
            for q in range(len(self.platforms_for_lvl[self.index_texture+sayd])):
                self.platforms.pop()
        for platform in self.platforms_for_lvl [self.index_texture]:
            self.platforms.append(platform)


    def append_and_kill_people(self,sayd):
        if sayd :
            self.run_man_enjay.clear()
            for q in range(len(self.run_man_for_lvl[self.index_texture+sayd])):
                self.run_man.pop()
        for platform in self.run_man_for_lvl [self.index_texture]:
            self.run_man.append(platform)
            self.run_man_enjay.append(arcade.PhysicsEnginePlatformer(platform,self.platforms,GRAVIT))
    
    def append_and_kill_snipers(self,sayd):
        if sayd :
            for q in range(len(self.sniper_for_lvl[self.index_texture+sayd])):
                self.list_sn.pop()
        for platform in self.sniper_for_lvl [self.index_texture]:
            self.list_sn.append(platform)


    def on_key_press (self, symbol: int, modifiers: int):
        if symbol==arcade.key.E:
            self.pulaa=Pula(self)
            self.pulaa.set_position(self.bill.center_x,self.bill.center_y+10)
            self.pula.append(self.pulaa)
            arcade.play_sound(self.shoot,0.5)
        if symbol==arcade.key.A:
            self.bill.change_x=-POWER_RUN
            self.bill.wolk=True
            self.bill.side=True
            self.bill.get_side()
        if symbol==arcade.key.D:
            self.bill.change_x=POWER_RUN
            self.bill.wolk=True
            self.bill.side=False
            self.bill.get_side()
        if symbol==arcade.key.SPACE:
            self.bill.down()
        if symbol==arcade.key.W and self.physics_engines.can_jump():
            self.physics_engines.jump(POWER_UP)
            arcade.play_sound(self.jump,1)
        
    

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol==arcade.key.A or  symbol==arcade.key.D:
            self.bill.change_x=0
            self.bill.wolk=False
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       print(x,y)


lon=Window(WIDHT,HEIGHT,TITLE)
arcade.run()
#разместить снайперов