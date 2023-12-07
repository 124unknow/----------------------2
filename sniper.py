import arcade

class R_bill(arcade.Sprite):
    def __init__(self,window):
        super().__init__("sniper/sniper_angle.png",1.1)
        self.window=window
        self.healf=4
        self.leftt=arcade.load_texture(f"sniper/sniper_forward.png")
        self.rightt=arcade.load_texture(f"sniper/sniper_forward.png",flipped_horizontally=True)
        self.l_angle=arcade.load_texture(f"sniper/sniper_angle.png")
        self.r_angle=arcade.load_texture(f"sniper/sniper_angle.png",flipped_horizontally=True)
        